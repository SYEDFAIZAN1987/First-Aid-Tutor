import os
from dotenv import load_dotenv
import openai
from gradio_client import Client

# Load API Key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"Using OpenAI API Key: {api_key[:5]}****{api_key[-3:]}")  
openai.api_key = api_key

# ---- STEP 1: Load First Aid Contextual Data ----
from langchain_community.document_loaders import ArxivLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import wandb
import pandas as pd

# Load medical and first aid papers from ArXiv
first_aid_docs = ArxivLoader(query="first aid treatment", load_max_docs=5).load()

# Split documents for indexing
text_splitter = RecursiveCharacterTextSplitter(chunk_size=250)
docs = text_splitter.split_documents(first_aid_docs)

# Create vectorstore
vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# ---- Define First Aid Questions ----
questions = [
    "What are the first aid measures for high fever in infants?",
    "What are the signs and symptoms of low blood sugar?",
    "What does RICE stand for in first aid treatment?",
    "What is the first aid treatment of bleeding?",
    "What is the first aid management of burns?",
    "What are the signs and symptoms of stroke?",
    "What is the treatment of snake bite?",
    "How do you provide first aid for choking?",
    "What are the immediate steps to treat a fainting patient?",
    "What are the First aid measures for taking care of a patient with insect stings and animal bites?"
]

# ---- STEP 2: Generate Ground Truth Responses using ChatGPT ----
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
prompt_template = """
Generate a detailed and accurate first-aid response based on the given context.

### CONTEXT
{context}

### QUESTION
{question}

### RESPONSE
"""
prompt = ChatPromptTemplate.from_template(prompt_template)

ground_truth_responses = []
for question in questions:
    retrieved_docs = retriever.invoke(question)
    context_text = "\n".join([doc.page_content for doc in retrieved_docs])
    generated_response = llm.invoke(prompt.format(context=context_text, question=question))
    ground_truth_responses.append(str(generated_response))

# ---- STEP 3: Fetch Responses from Deployed Chatbot ----
print("\n===== Fetching Responses from Chatbot =====")

client = Client("DrSyedFaizan/First_Aid_Assistant")
responses = []

for question in questions:
    try:
        result = client.predict(chatbot=[], message=question, api_name="/respond")
        chat_history = result[1]  
        chatbot_response = next((entry["content"] for entry in chat_history if entry["role"] == "assistant"), "[NO RESPONSE]")
    except Exception as e:
        chatbot_response = f"[ERROR: {e}]"
    
    responses.append(str(chatbot_response))

# Save bot responses to a text file
with open("bot_responses.txt", "w", encoding="utf-8") as f:
    for q, r in zip(questions, responses):
        f.write(f"Q: {q}\nA: {r}\n\n")

# Print chatbot responses for debugging
for q, r in zip(questions, responses):
    print(f"Q: {q}\nA: {r}\n")

# ---- STEP 5: Evaluate Using RAGAS ----
from datasets import Dataset
import pandas as pd
from tqdm import tqdm
from ragas import evaluate
from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_recall,
    answer_correctness,
    answer_similarity
)

def create_ragas_dataset(eval_dataset):
    """Convert dataset to RAGAS format."""
    df = eval_dataset.to_pandas()
    rag_dataset = []
    for _, row in df.iterrows():
        rag_dataset.append(
            {
                "question": row["question"],
                "answer": row["answer"],
                "contexts": ["First aid medical references"],
                "ground_truths": [row["ground_truth"]],
                "reference": row["context"]
            }
        )
    rag_df = pd.DataFrame(rag_dataset)
    return Dataset.from_pandas(rag_df)

def evaluate_ragas_dataset(ragas_dataset):
    """Run RAGAS evaluation with proper handling of required_columns."""
    try:
        result = evaluate(
            ragas_dataset,
            metrics=[
                faithfulness,
                answer_relevancy,
                context_recall,
                answer_correctness,
                answer_similarity
            ],
        )
        return result
    except Exception as e:
        print("⚠️ RAGAS Error:", e)
        raise e

# Create ground truth dataset
ground_truth_qac_set = pd.DataFrame({
    "question": questions,
    "answer": responses,
    "context": ["First aid medical references"] * len(questions),
    "ground_truth": [str(response) for response in ground_truth_responses],
    "reference": ["First aid medical references"] * len(questions)
})

eval_dataset = Dataset.from_pandas(ground_truth_qac_set.astype(str))

# Save evaluation datasets
eval_dataset.to_csv("groundtruth_eval_dataset.csv")
basic_qa_ragas_dataset = create_ragas_dataset(eval_dataset)
basic_qa_ragas_dataset.to_csv("basic_qa_ragas_dataset.csv")

# Run evaluation
basic_qa_result = evaluate_ragas_dataset(basic_qa_ragas_dataset)

print("\n===== Evaluation Results =====")
print(basic_qa_result)

evaluation_results = basic_qa_result.to_pandas()

# Save evaluation results as log

# ---- STEP 6: Log Results to WandB ----

import wandb
import pandas as pd

# ✅ Convert `eval_dataset` (Dataset) to Pandas DataFrame
eval_df = eval_dataset.to_pandas()

# ✅ Convert `basic_qa_ragas_dataset` (Dataset) to Pandas DataFrame
ragas_df = basic_qa_ragas_dataset.to_pandas()

# ✅ Save DataFrames as CSV
eval_df.to_csv("groundtruth_eval_dataset.csv", index=False)
ragas_df.to_csv("basic_qa_ragas_dataset.csv", index=False)

# ✅ Initialize WandB
wandb.init(
    project="first-aid-tutor",
    entity="drsyedfaizan1987-northeastern-university",
    name="ragas_evaluation",
    notes="Logging evaluation datasets for first-aid chatbot.",
    tags=["first-aid", "evaluation", "ragas"]
)

# ✅ Log DataFrames to WandB as Tables
wandb.log({"basic_qa_ragas_dataset": wandb.Table(dataframe=evaluation_results)})
wandb.log({"groundtruth_eval_dataset": wandb.Table(dataframe=eval_df)})
wandb.log({"basic_qa_ragas_dataset": wandb.Table(dataframe=ragas_df)})

# ✅ Finish WandB run
wandb.finish()
