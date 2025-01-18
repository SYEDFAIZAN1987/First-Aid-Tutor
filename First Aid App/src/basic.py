from gradio_client import Client

# Connect to Hugging Face API
client = Client("DrSyedFaizan/First_Aid_Assistant")

# Define test question
test_question = "What are the first aid measures for high fever in infants?"

# Make API call with correct formatting
try:
    result = client.predict(
        chatbot=[],  # Ensure chatbot history is correctly formatted
        message=test_question,  # The actual question
        api_name="/respond"
    )

    # Extract assistant response
    chat_history = result[1]  # Full chat history
    chatbot_response = next((entry["content"] for entry in chat_history if entry["role"] == "assistant"), "[NO RESPONSE]")

    # Print extracted response
    print("\n===== Response from Chatbot =====")
    print("Chatbot says:", chatbot_response)
except Exception as e:
    print("Error:", e)
