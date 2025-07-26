# backend/main.py
# Main.py

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List
from db import conversations  # Make sure db.py exists and has `conversations`

app = FastAPI()

# Define Pydantic models
class Message(BaseModel):
    sender: str
    text: str
    timestamp: datetime

class Session(BaseModel):
    session_id: str
    messages: List[Message]

class Conversation(BaseModel):
    user_id: str
    sessions: List[Session]

# POST endpoint to save a conversation
@app.post("/conversation/")
def save_conversation(conv: Conversation):
    conversations.insert_one(conv.dict())
    return {"message": "Conversation saved"}

# GET endpoint to retrieve a conversation by user_id
@app.get("/conversation/{user_id}")
def get_conversation(user_id: str):
    result = conversations.find_one({"user_id": user_id})
    if result:
        result["_id"] = str(result["_id"])  # Convert ObjectId to string
        return result
    return {"message": "Not found"}