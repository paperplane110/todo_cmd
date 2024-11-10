import os
import json

from rich.console import Console

import todo_cmd.templates as t
from todo_cmd.sub_cmd.init_todo import main as init_todo

console = Console()

# Load configuration
TODO_FOLDER = os.path.join(os.path.expanduser('~'), '.todo')
CONFIG_FILE = os.path.join(TODO_FOLDER, "config.json")


def read_config() -> dict:
    conf = None
    try:
        with open(CONFIG_FILE, "r") as f:
            conf = json.load(f)
    except FileNotFoundError:
        console.print(t.error("~/.todo/config.json 文件不存在, 请初始化配置 [b cyan3]todo[/]"))
        console.print(t.error("~/.todo/config.json file not found, please run [b cyan3]todo[/]"))
        init_todo()
    finally:
        with open(CONFIG_FILE, "r") as f:
            conf = json.load(f)
    return conf

CONFIG = read_config()
