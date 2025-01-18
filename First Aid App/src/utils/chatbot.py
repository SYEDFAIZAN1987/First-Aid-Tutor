import gradio as gr
import os
import openai
import re
import html
from typing import List, Tuple
from langchain_chroma import Chroma  # ✅ Updated import
from utils.load_config import LoadConfig

# Load configuration
APPCFG = LoadConfig()

# OpenAI Client
client = openai.OpenAI()

class ChatBot:
    """
    Chatbot class that only retrieves answers from a pre-uploaded document stored in ChromaDB.
    """

    @staticmethod
    def respond(chatbot: List, message: str) -> Tuple:
        """
        Retrieve an answer strictly from the pre-uploaded document.
        If no relevant information is found, return a "no answer found" message.
        """
        # Ensure the pre-processed document database exists
        if not os.path.exists(APPCFG.persist_directory):
            chatbot.append({"role": "assistant", "content": "⚠️ No document database found. Please ensure the First Aid PDF is preloaded."})
            return "", chatbot

        # Load ChromaDB with stored document embeddings
        vectordb = Chroma(persist_directory=APPCFG.persist_directory, embedding_function=APPCFG.embedding_model)
        docs = vectordb.similarity_search(message, k=APPCFG.k)

        if not docs:
            chatbot.append({"role": "assistant", "content": "⚠️ No relevant answer found in the document."})
            return "", chatbot

        # Extract retrieved content
        retrieved_content = ChatBot.clean_references(docs)
        chat_history = f"Chat history:\n {str(chatbot[-APPCFG.number_of_q_a_pairs:])}\n\n"
        prompt = f"{chat_history}{retrieved_content}# User question:\n{message}"

        # Generate response using OpenAI GPT
        response = client.chat.completions.create(
            model=APPCFG.llm_engine,
            messages=[
                {"role": "system", "content": "Answer only using the First Aid document. If unsure, say 'I don't know'."},
                {"role": "user", "content": prompt}
            ]
        )

        chatbot.append({"role": "user", "content": message})  # ✅ User input
        chatbot.append({"role": "assistant", "content": response.choices[0].message.content})  # ✅ AI response

        return "", chatbot

    @staticmethod
    def clean_references(documents: List) -> str:
        """
        Extract and format relevant content from retrieved documents.
        """
        cleaned_content = []
        for doc in documents:
            # ✅ Ensure correct extraction of content and metadata
            content = doc.page_content
            metadata = doc.metadata

            # ✅ Handle missing metadata safely
            source = metadata.get('source', 'Unknown source')
            page_number = metadata.get('page', 'Unknown page')

            cleaned_content.append(
                f"📄 Page {page_number}: {content}\n📌 Source: {source}\n"
            )

        return "\n".join(cleaned_content)
