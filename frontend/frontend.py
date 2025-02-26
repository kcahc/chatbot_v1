from nicegui import ui
import requests

# Function to send the message to the FastAPI endpoint
def send_message():
    user_input = input_field.value
    try:
        # POST request to the backend chat endpoint with query parameters
        response = requests.post("http://127.0.0.1:8000/chat", params={"prompt": user_input}).json()
        chat_area.value += f"You: {user_input}\nLlama: {response['response']['content']}\n\n"
        chat_area.update()
        input_field.value = ""  # Clear the input field
        input_field.update()  # Update the input field UI
    except Exception as e:
        chat_area.value += f"Error: {str(e)}\n\n"
        chat_area.update()

ui.label("Llama 3.2 Chatbot")
chat_area = ui.textarea(label="Chat History", value="").style('height: 600px; width: 600px').props('readonly')
input_field = ui.input(label="Type your message here").style('width: 600px')
ui.button("Send", on_click=send_message)

ui.run()
