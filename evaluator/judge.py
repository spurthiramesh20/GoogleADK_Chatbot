import json
from pathlib import Path
import litellm


def llm_judge(user_input, bot_response):
    prompt_path = Path(__file__).resolve().parent / "judge_prompt.yml"
    prompt = prompt_path.read_text(encoding="utf-8")

    filled_prompt = prompt.format(
        user_input=user_input,
        bot_response=bot_response
    )

    response = litellm.completion(
        model="groq/llama-3.1-8b-instant",   # ✅ Groq model
        messages=[
            {"role": "user", "content": filled_prompt}
        ],
        temperature=0
    )

    return json.loads(
        response["choices"][0]["message"]["content"]
    )