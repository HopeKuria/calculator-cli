import json

def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

def load_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
HISTORY_FILE = "history.json"