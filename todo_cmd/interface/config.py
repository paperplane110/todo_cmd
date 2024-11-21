import os
import json

import todo_cmd.templates as t
from todo_cmd.sub_cmd.init_todo import main as init_todo


# Load configuration
TODO_FOLDER = os.path.join(os.path.expanduser('~'), '.todo')
CONFIG_FILE = os.path.join(TODO_FOLDER, "config.json")


def read_config() -> dict:
    conf = None
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            conf = json.load(f)
    except FileNotFoundError:
        t.error("~/.todo/config.json 文件不存在, 请初始化配置 [b cyan3]todo[/]")
        t.error("~/.todo/config.json file not found, please run [b cyan3]todo[/]")
        init_todo()
    finally:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            conf = json.load(f)
    return conf


def val_attr_value(attr: str, value: str) -> bool:
    if attr == "lang":
        if value not in ["zh", "en"]:
            t.error("language should be either 'zh' or 'en'")
            return False
    elif attr == "ddl_delta":
        if not value.isdigit():
            t.error("ddl_delta should be an integer and larger than 0")
            return False
        elif int(value) < 0:
            t.error("ddl_delta should be an integer and larger than 0")
            return False
    else:
        pass
    return True


def set_config(attr: str, value):
    if not val_attr_value:
        return 1
    config = read_config()
    config[attr] = value
    with open(CONFIG_FILE, "w") as fp:
        json.dump(config, fp, indent=2)
    t.done(f"Set config done: {attr} = {value}")


CONFIG = read_config()
