import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evaluator import run_evaluation
from evaluator.adk_adapter import adk_adapter

with open("test_cases.json") as f:
    test_cases = json.load(f)

results = run_evaluation(adk_adapter, test_cases)

for r in results:
    print(r)
