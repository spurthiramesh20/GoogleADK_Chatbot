import logging
from pathlib import Path
from typing import Optional
from google.genai.types import Content

from google.genai import types
from src.agent import runner

from dotenv import load_dotenv
from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Load environment variables
_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(dotenv_path=_ROOT / ".env")

# Import the runner from your ADK agent.py
from src.agent import runner

# Silence excessive logging
logging.getLogger("httpx").setLevel(logging.WARNING)

api = FastAPI(title=" Support Chatbot - Google ADK")

class ChatRequest(BaseModel):
    message: str
    thread_id: Optional[str] = "local_test"

class ChatResponse(BaseModel):
    reply: str

@api.get("/health")
def health() -> dict:
    return {"status": "ok"}

@api.get("/", response_class=HTMLResponse)
def index() -> str:
    html_path = Path(__file__).parent / "index.html"
    return html_path.read_text(encoding="utf-8")

@api.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    try:
        # 1. Prepare message
        user_content = types.Content(
            role="user",
            parts=[types.Part(text=req.message)]
        )

        # 2. Start the async stream
        event_stream = runner.run_async(
            user_id="igot_user",
            session_id=req.thread_id,
            new_message=user_content
        )

        reply_text = ""
        # 3. Iterate through EVERY event in the stream
        async for event in event_stream:
            # DEBUG: Print to terminal to see what's happening behind the scenes
            if event.get_function_calls():
                print(f"DEBUG: Agent is calling tool: {event.get_function_calls()[0].name}")

            # Collect any text parts as they arrive
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        # Append text because a turn might have multiple chunks
                        reply_text += part.text

            # If this is the official end of the turn, we can stop
            if event.is_final_response():
                # If we have text, we are done
                if reply_text.strip():
                    break

        return ChatResponse(reply=reply_text.strip() or "I'm sorry, I'm having trouble connecting to the support protocols.")

    except Exception as e:
        print(f"CRITICAL ADK ERROR: {e}")
        return ChatResponse(reply="Connection error. Please try again.")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="0.0.0.0", port=8001)