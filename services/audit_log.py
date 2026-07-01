import json
import os

LOG_FILE = "data/audit_log.json"


def load_log():
    if not os.path.exists(LOG_FILE):
        return []

    try:
        with open(LOG_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_entry(entry):
    log = load_log()
    log.append(entry)

    with open(LOG_FILE, "w") as file:
        json.dump(log, file, indent=4)