# Clara Automation Pipeline

## Overview

This project implements a zero-cost automation pipeline that converts demo call transcripts into structured configuration artifacts for a Clara voice agent.

The system processes demo call transcripts and generates:

* Structured **Account Memo JSON**
* **Retell Agent Draft Specification**
* Versioned outputs for **v1 (demo)** and **v2 (onboarding updates)**

The goal is to simulate the real Clara onboarding automation workflow.

---

## Architecture

```
Transcript
   ↓
extract_account_data.py
   ↓
Account Memo JSON
   ↓
generate_agent_spec.py
   ↓
Retell Agent Draft Spec
   ↓
Stored in outputs/accounts/<account_id>/v1
```

---

## Repository Structure

```
dataset/
    bens-electric-demo.txt

scripts/
    extract_account_data.py
    generate_agent_spec.py
    run_pipeline.py

outputs/
    accounts/
        bens-electric/
            v1/
            v2/

workflows/
changelog/
```

---

## How to Run the Pipeline

1. Clone the repository.

2. Ensure Python is installed.

3. Run the pipeline script:

```
python scripts/run_pipeline.py
```

4. Generated outputs will appear in:

```
outputs/accounts/bens-electric/v1/
```

Files generated:

* account_memo.json
* agent_spec.json

---

## Versioning

* **v1** → Generated from demo call transcript
* **v2** → Updated configuration after onboarding call

---

## Key Features

* Zero-cost implementation
* Structured JSON configuration generation
* Versioned agent configurations
* Simple and reproducible automation pipeline

---

## Future Improvements

With production access the following improvements could be added:

* LLM-based transcript extraction
* Supabase database storage
* Automated Retell API integration
* Diff viewer for v1 → v2 changes
* Dashboard for account management

---

## Author

Sudha Lahari Ganti

                ┌────────────────────────┐
                │ Demo Call Transcript   │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │ extract_account_data.py │
                │ Extract structured data │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │ Account Memo JSON      │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │ generate_agent_spec.py │
                │ Build agent config     │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │ Retell Agent Draft Spec│
                └────────────┬───────────┘
                             │
                             ▼
                outputs/accounts/bens-electric/v1
<img width="1408" height="768" alt="AI Automation Project" src="https://github.com/user-attachments/assets/56d7a293-58ff-4b1c-bb1e-c77713440498" />
