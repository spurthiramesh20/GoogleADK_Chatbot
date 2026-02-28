import os
import yaml
import httpx
from pathlib import Path
from dotenv import load_dotenv 
from openai import AsyncOpenAI
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from src.tools import TOOLS

# 2. Load the .env file IMMEDIATELY
load_dotenv()

# 3. Load System Prompt
PROMPT_PATH = Path(__file__).parent / "prompts" / "prompt.yml"
with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    PROMPT_DATA = yaml.safe_load(f)
SYSTEM_PROMPT = PROMPT_DATA["v1"]["system"]

# 4. Configure LiteLLM Proxy Client
# We use a direct check to ensure the key isn't None
api_key = os.getenv("GEMINI_API_KEY")
proxy_client = AsyncOpenAI(
    api_key=api_key,
    base_url=os.getenv("GEMINI_BASE_URL"), 
    http_client=httpx.AsyncClient(verify=False) 
)

# 5. Define the Agent
agent = LlmAgent(
    name="iGOT_Support_Agent",
    model=LiteLlm(
        model=os.getenv("GEMINI_MODEL", "gemini-flash"),
        client=proxy_client,
        custom_llm_provider="openai"
    ),
    instruction=SYSTEM_PROMPT,
    tools=TOOLS
)

# 6. Initialize Session & Runner
session_service = InMemorySessionService()
runner = Runner(
    app_name="iGOT_Support_App",
    agent=agent,
    session_service=session_service,
    auto_create_session=True
)