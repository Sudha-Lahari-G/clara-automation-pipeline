import json
import sys

def generate_agent_spec(memo):

    agent_spec = {
        "agent_name": memo.get("company_name", "Clara Agent"),
        "voice_style": "professional and calm",

        "key_variables": {
            "timezone": memo.get("business_hours", {}).get("timezone", ""),
            "business_hours": memo.get("business_hours", {}),
            "office_address": memo.get("office_address", ""),
            "emergency_definition": memo.get("emergency_definition", [])
        },

        "system_prompt": f"""
You are Clara, an AI voice assistant for {memo.get("company_name","the company")}.

BUSINESS HOURS FLOW
- Greet the caller
- Ask the reason for calling
- Collect name and phone number
- Route or transfer call
- If transfer fails, apologize and assure follow-up
- Ask if anything else is needed
- Close politely

AFTER HOURS FLOW
- Greet caller
- Ask purpose
- Confirm if emergency
- If emergency:
    collect name
    collect phone
    collect address
    attempt transfer
- If transfer fails:
    apologize and assure quick follow-up
- If non-emergency:
    collect details for next business day
- Ask if anything else is needed
- Close call
""",

        "call_transfer_protocol": "Attempt transfer to technician. Retry once if needed.",
        "fallback_protocol": "If transfer fails, assure caller that a technician will call back.",
        "version": "v1"
    }

    return agent_spec


if __name__ == "__main__":

    memo_file = sys.argv[1]

    with open(memo_file, "r") as f:
        memo = json.load(f)

    agent_spec = generate_agent_spec(memo)

    print(json.dumps(agent_spec, indent=2))
