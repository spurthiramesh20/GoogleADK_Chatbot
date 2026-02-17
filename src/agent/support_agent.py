import yaml
from pathlib import Path

from src.tools.support_tools import (
    classify_intent,
    handle_certificate_issue,
    handle_course_issue,
    handle_login_issue,
)


PROMPT_PATH = Path(__file__).parents[1] / "prompts" / "support_prompts.yml"
PROMPTS = yaml.safe_load(PROMPT_PATH.read_text(encoding="utf-8")) or {}
SYSTEM_PROMPT = PROMPTS.get("v2", PROMPTS.get("v1", {})).get("system", "")


class SimpleSupportAgent:
    def __init__(self, system_prompt: str) -> None:
        self.system_prompt = system_prompt

    def run(self, message: str) -> str:
        if not message or not message.strip():
            return "Please enter your question so I can help."

        intent = classify_intent(message)
        if intent == "login":
            return handle_login_issue(message)
        if intent == "course":
            return handle_course_issue(message)
        if intent == "certificate":
            return handle_certificate_issue(message)

        return (
            "I can help with iGOT login, course access, or certificate issues. "
            "Which one are you facing?"
        )


igot_agent = SimpleSupportAgent(system_prompt=SYSTEM_PROMPT)
