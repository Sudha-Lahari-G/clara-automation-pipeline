import json
import subprocess
import os

TRANSCRIPT_PATH = "dataset/bens-electric-demo.txt"
ACCOUNT_ID = "bens-electric"

OUTPUT_DIR = f"outputs/accounts/{ACCOUNT_ID}/v1"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Step 1: Generate Account Memo
memo_output = subprocess.check_output([
    "python",
    "scripts/extract_account_data.py",
    TRANSCRIPT_PATH,
    ACCOUNT_ID
])

memo_json = json.loads(memo_output)

memo_path = f"{OUTPUT_DIR}/account_memo.json"

with open(memo_path, "w") as f:
    json.dump(memo_json, f, indent=2)

print("Account memo generated")

# Step 2: Generate Agent Spec
agent_output = subprocess.check_output([
    "python",
    "scripts/generate_agent_spec.py",
    memo_path
])

agent_json = json.loads(agent_output)

agent_path = f"{OUTPUT_DIR}/agent_spec.json"

with open(agent_path, "w") as f:
    json.dump(agent_json, f, indent=2)

print("Agent spec generated")
