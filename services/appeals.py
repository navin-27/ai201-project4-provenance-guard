import json
import os

LOG_FILE = "data/audit_log.json"


def submit_appeal(content_id, reasoning):

    if not os.path.exists(LOG_FILE):
        return False

    with open(LOG_FILE, "r") as file:
        entries = json.load(file)

    updated = False

    for entry in entries:

        if entry["content_id"] == content_id:

            entry["status"] = "under_review"
            entry["appeal_reasoning"] = reasoning

            updated = True
            break

    with open(LOG_FILE, "w") as file:
        json.dump(entries, file, indent=4)

    return updated