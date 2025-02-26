from fastapi import FastAPI
import ollama

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Llama 3.2 Chatbot API is running!"}

@app.post("/chat")
def chat_with_llama(prompt: str):
    # This assumes the ollama.chat call accepts a 'model' and a list of messages.
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]}

        