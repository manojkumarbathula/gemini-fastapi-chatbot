import os
from fastapi import FastAPI
from google import genai 
from dotenv import load_dotenv
from pydantic import BaseModel
from google.genai import types

load_dotenv()
app=FastAPI()

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class QuestionRequest(BaseModel):
    question:str
    
@app.post("/ask-ai")
def ask_ai(request:QuestionRequest):
    response=client.models.generate_content(
            model="gemini-3.6-flash",
            contents=request.question
    )
    return {
        "answer":response.text
    }
    
class ChatRequest(BaseModel):
    message:str

conversation=[]

instructions="""
you are a FastAPI Tutor
  - FastAPI
  - API Development
  - Pydantic
If the user asks something unrelated to these topics,
response: I can only help with FastAPI
"""
@app.post("/chat")
def chat_bot(request: ChatRequest):

    conversation.append({
        "role": "user",
        "parts": [
            {
                "text": request.message
            }
        ]
    })

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=conversation,
        config=types.GenerateContentConfig(
            system_instruction=instructions
        )
    )

    answer = response.text

    conversation.append({
        "role": "model",
        "parts": [
            {
                "text": answer
            }
        ]
    })

    return {
        "res": answer
    }