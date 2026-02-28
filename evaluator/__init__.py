from __future__ import annotations

from typing import Any, Callable, Dict, List

from .judge import llm_judge


def run_evaluation(adapter: Callable[[str], Any], test_cases: List[Dict[str, Any]]):
    results = []

    for i, case in enumerate(test_cases, start=1):
        user_input = case.get("input") or case.get("user_input")
        if not user_input:
            raise ValueError(f"Test case {i} missing 'input' or 'user_input'")

        bot = adapter(user_input)
        if isinstance(bot, dict):
            bot_text = bot.get("text", "")
        else:
            bot_text = str(bot)

        scores = llm_judge(user_input, bot_text)

        results.append(
            {
                "input": user_input,
                "response": bot_text,
                "scores": scores,
                "meta": {k: v for k, v in (bot.items() if isinstance(bot, dict) else []) if k != "text"},
            }
        )

    return results
