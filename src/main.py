from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from src.agent.support_agent import igot_agent

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
def home():
    index_path = Path(__file__).parent / "index.html"
    with index_path.open("r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
def chat(req: ChatRequest):
    response = igot_agent.run(req.message)
    return {"reply": response}
