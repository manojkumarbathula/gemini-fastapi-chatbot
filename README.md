# AI FastAPI Tutor

An AI-powered FastAPI application integrated with Google's Gemini API.
The application provides direct AI question answering and a conversational
FastAPI tutor with controlled system instructions.

## Features

- AI question answering using Gemini API
- Conversational chatbot with conversation history
- FastAPI REST API endpoints
- Pydantic request validation
- System instructions for domain-specific responses
- Environment-based API key configuration

## Tech Stack

- Python
- FastAPI
- Pydantic
- Google Gemini API
- python-dotenv
- Uvicorn

## API Endpoints

### 1. Ask AI

**POST** `/ask-ai`

Request:

```json
{
  "question": "What is FastAPI?"
}
{
  "answer": "FastAPI is a modern Python web framework..."
}
2. Chat with AI Tutor

POST /chat

Request:

{
  "message": "What is Pydantic?"
}

Response:

{
  "res": "Pydantic is used for data validation..."
}
Setup
1. Clone the repository
git clone https://github.com/manojkumarbathula/gemini-fastapi-chatbot.git
cd gemini-fastapi-chatbot
2. Create virtual environment
python -m venv venv
3. Activate virtual environment

Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Configure environment variables

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key
6. Run the application
uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs
Project Structure
ai-fastapi-tutor/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
Future Improvements
User-specific conversation history
Persistent conversation storage
Authentication and authorization
Better error handling
Production deployment
Automated testing

### 3️⃣ GitHub ki push cheyyali

Save chesi:

```bash
git add README.md
