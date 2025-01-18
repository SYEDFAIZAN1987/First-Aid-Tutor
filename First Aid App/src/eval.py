import numpy as np
import matplotlib.pyplot as plt
from gradio_client import Client
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score, f1_score
from huggingface_hub import HfApi
# ========== STEP 1: Define Test Questions and Expected Answers ==========
questions = [
    "What are the first aid measures for high fever in infants?",
    "How should you treat a patient with low blood sugar?",
    "What does RICE stand for in first aid treatment?",
    "How should you manage a snake bite before reaching a hospital?",
    "What are the symptoms of shock and how do you treat it?",
    "How should you respond to a person experiencing a seizure?",
    "What should be done if someone is choking?",
    "How do you provide first aid for minor burns?",
    "What are the immediate steps to treat a fainting patient?",
    "How should you respond to a dog bite to prevent rabies?",
]

expected_responses = [
    "For infants with a high fever: For infants 0-3 months with a rectal temperature of 100.4°F (38°C) or higher, refer to the doctor. "
    "For infants 3-6 months with a rectal temperature up to 102°F (38.9°C), encourage rest and plenty of fluids; medication is not needed but refer to the doctor if the child seems unusually irritable, lethargic, or uncomfortable.",

    "Provide sugar-containing liquids like fruit juice or 5-6 hard candies. If unconscious, place glucose powder under their tongue and refer them immediately to a hospital.",

    "RICE stands for Rest, Ice, Compression, and Elevation. It is used to treat sprains, strains, fractures, and joint dislocations.",

    "Lay the patient down and keep them calm. Apply a tourniquet above the bite site, loosening it every 10 minutes. "
    "Wash the wound gently with saline or antiseptic lotion and apply a clean dressing. "
    "Immobilize the affected limb and apply ice packs. Transport the patient to a hospital immediately.",

    "Symptoms of shock include pale, clammy skin, rapid pulse, dizziness, and weakness. "
    "First aid measures involve laying the patient down, elevating their legs, covering them with a blanket, stopping any bleeding, "
    "and giving sugar water if they are conscious. Immediate hospital transfer is required.",

    "Ensure the person is in a safe area. Do not restrain their movements or put anything in their mouth. "
    "Loosen tight clothing and turn them on their side after the seizure ends. "
    "Call for medical assistance if the seizure lasts longer than five minutes or repeats.",

    "For a choking adult, stand behind them and perform the Heimlich maneuver: wrap arms around their waist, "
    "place a fist slightly above the navel, and thrust upwards. For infants, hold them upside down and slap their back.",

    "Run the burned area under cold water or apply an ice pack until the pain subsides. "
    "Clean and bandage the burn to prevent infection. For chemical burns, rinse the affected area for 15-20 minutes with water.",

    "If a person faints, lay them flat for at least 15 minutes. Raise their legs above the heart level. "
    "Loosen any restrictive clothing and check their breathing. If they remain unconscious, call emergency services.",

    "For a known dog, wash the wound thoroughly with soap and water, apply antiseptic, and give a tetanus toxoid injection. "
    "If the dog is unknown, refer the patient to a doctor immediately for an anti-rabies vaccine.",
]

# ========== STEP 2: Query Chatbot ==========
print("\n===== Fetching Responses from Chatbot =====")

client = Client("DrSyedFaizan/First_Aid_Assistant")
responses = []

for question in questions:
    try:
        result = client.predict(chatbot=[], message=question, api_name="/respond")
        chat_history = result[1]  # Extract chat history
        chatbot_response = next((entry["content"] for entry in chat_history if entry["role"] == "assistant"), "[NO RESPONSE]")
    except Exception as e:
        chatbot_response = f"[ERROR: {e}]"
    
    responses.append(chatbot_response)

# Print chatbot responses for debugging
for q, r in zip(questions, responses):
    print(f"Q: {q}\nA: {r}\n")

# ========== STEP 3: Compute Similarity Scores ==========
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(expected_responses + responses)

expected_vectors = tfidf_matrix[:len(expected_responses)]
response_vectors = tfidf_matrix[len(expected_responses):]

similarity_scores = cosine_similarity(expected_vectors, response_vectors).diagonal()

# Print Similarity Scores
print("\n===== Similarity Scores =====")
for i, score in enumerate(similarity_scores):
    print(f"Q: {questions[i]}\nSimilarity: {score:.4f}")

# ========== STEP 4: Compute Evaluation Metrics ==========
expected_binary = [1] * len(questions)
actual_binary = [1 if responses[i] != "[NO RESPONSE]" else 0 for i in range(len(questions))]

precision = precision_score(expected_binary, actual_binary, zero_division=1)
recall = recall_score(expected_binary, actual_binary, zero_division=1)
f1 = f1_score(expected_binary, actual_binary, zero_division=1)

# Print and save results
print("\n===== Evaluation Results =====")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

# ========== STEP 5: Visualization ==========
plt.figure(figsize=(8, 5))
plt.bar(["Precision", "Recall", "F1 Score"], [precision, recall, f1], color=["blue", "green", "red"])
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Chatbot Evaluation Metrics")
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Save the plot
evaluation_plot_path = "evaluation_plot.png"
plt.savefig(evaluation_plot_path)
plt.show()

# ========== STEP 6: Upload to Hugging Face ==========
hf_api = HfApi()
repo_id = "DrSyedFaizan/First_Aid_Assistant_Evaluation"

# Ensure repository exists or create it
try:
    hf_api.create_repo(repo_id, exist_ok=True)
except Exception as e:
    print(f"Error creating repo: {e}")

# Upload evaluation results
evaluation_results_path = "evaluation_results.txt"
with open(evaluation_results_path, "w") as f:
    f.write(f"Precision: {precision:.4f}\n")
    f.write(f"Recall: {recall:.4f}\n")
    f.write(f"F1 Score: {f1:.4f}\n")

hf_api.upload_file(path_or_fileobj=evaluation_results_path, path_in_repo="evaluation_results.txt", repo_id=repo_id)
hf_api.upload_file(path_or_fileobj=evaluation_plot_path, path_in_repo="evaluation_plot.png", repo_id=repo_id)

print("\nUploaded evaluation results and visualization to Hugging Face!")

