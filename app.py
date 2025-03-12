import requests
import json
from flask import Flask
from flask_socketio import SocketIO, emit
import eventlet
from dotenv import load_dotenv
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Hugging Face API Details
load_dotenv()
API_URL = "https://api-inference.huggingface.co/models/gpt2"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_KEY')}"}


def query_huggingface_api(prompt, max_length=100):
    payload = {
        "inputs": prompt,
        "parameters": {"max_length": max_length}
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    return "Sorry, I couldn't generate a response."

@socketio.on("message")
def handle_message(data):
    print(f"Received message: {data}")
    response = query_huggingface_api(data)
    emit("response", response)

@app.route('/')
def index():
    return "WebSocket Server Running with Hugging Face Integration"

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)




