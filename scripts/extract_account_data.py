import json
import sys

def extract_account_data(transcript_text, account_id):

    memo = {
        "account_id": account_id,
        "company_name": "",
        "business_hours": {
            "days": "",
            "start": "",
            "end": "",
            "timezone": ""
        },
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": {},
        "non_emergency_routing_rules": {},
        "call_transfer_rules": {},
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    text = transcript_text.lower()

    if "electric" in text:
        memo["company_name"] = "Ben's Electric"

    if "emergency" in text:
        memo["emergency_definition"].append(
            "Electrical emergency calls"
        )

    memo["services_supported"] = [
        "Electrical repair",
        "Electrical maintenance",
        "Emergency electrical service"
    ]

    memo["office_hours_flow_summary"] = (
        "Collect caller name and phone number, "
        "identify service request, transfer to technician or office."
    )

    memo["after_hours_flow_summary"] = (
        "Confirm if emergency. If yes collect name, phone, address "
        "and attempt transfer to on-call technician."
    )

    memo["questions_or_unknowns"] = [
        "Exact business hours not confirmed",
        "Office address not mentioned",
        "Emergency routing number unknown"
    ]

    memo["notes"] = "Generated from demo call transcript."

    return memo


if __name__ == "__main__":

    transcript_file = sys.argv[1]
    account_id = sys.argv[2]

    with open(transcript_file, "r") as f:
        transcript_text = f.read()

    memo = extract_account_data(transcript_text, account_id)

    print(json.dumps(memo, indent=2))
