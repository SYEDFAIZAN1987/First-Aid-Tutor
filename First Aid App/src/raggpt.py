import gradio as gr
from utils.chatbot import ChatBot


# Define CSS styles for a clean and modern UI
custom_css = """
body {
    background: linear-gradient(to right, #004aad, #00a2ff);
    color: white;
    font-family: 'Poppins', sans-serif;
}

h1 {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: white;
    text-shadow: 2px 2px 10px rgba(255, 255, 255, 0.5);
    margin-bottom: 20px;
}

#chatbot {
    background: #dfe9ff;
    border-radius: 15px;
    padding: 15px;
    color: #003366;
    font-size: 16px;
    min-height: 500px;
    border: 2px solid #003366;
    box-shadow: 0 0 10px rgba(0, 162, 255, 0.6);
}

input {
    border-radius: 8px;
    padding: 10px;
    font-size: 16px;
    border: 2px solid #007bff;
    background-color: #eef6ff;
    color: #003366;
}

button {
    background-color: #003366;
    color: white;
    border-radius: 8px;
    padding: 12px 18px;
    border: none;
    cursor: pointer;
    font-weight: bold;
    transition: 0.3s ease-in-out;
    box-shadow: 0px 4px 8px rgba(255, 255, 255, 0.2);
}

button:hover {
    background-color: #00a2ff;
    box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.4);
}

.gradio-container {
    max-width: 900px;
    margin: auto;
    padding: 20px;
    text-align: center;
}
"""

# Define the chatbot UI with only input and response
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("<h1>🚑 First Aid Tutor</h1>")

    chatbot = gr.Chatbot([], elem_id="chatbot", bubble_full_width=False, height=500, type="messages")

    user_input = gr.Textbox(
        label="💬 Ask a First Aid Question:",
        placeholder="Type your question here...",
    )

    submit_button = gr.Button("🚀 Get First Aid Advice")

    submit_button.click(
        fn=ChatBot.respond,
        inputs=[chatbot, user_input],  # Only chatbot & input
        outputs=[user_input, chatbot],
    )

if __name__ == "__main__":
    demo.launch(share=True)
