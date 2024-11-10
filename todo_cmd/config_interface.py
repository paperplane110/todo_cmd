import os
import json

from todo_cmd.init_todo import main as init_todo

# Load configuration
TODO_FOLDER = os.path.join(os.path.expanduser('~'), '.todo')
CONFIG_FILE = os.path.join(TODO_FOLDER, "config.json")

def read_config() -> dict:
    try:
        with open(CONFIG_FILE, "r") as f:
            conf = json.load(f)
    except Exception as e:
        init_todo()
    return conf
