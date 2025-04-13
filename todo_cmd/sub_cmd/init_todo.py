"""
When the user first time uses `todo`,
init `config.json` and `todo.json` in ~/.todo/
"""
import os
import json

from rich.prompt import Confirm

import todo_cmd.templates as t


TODO_FOLDER = os.path.join(os.path.expanduser('~'), '.todo')
TODO_FILE = os.path.join(TODO_FOLDER, 'todo.json')
CONFIG_FILE = os.path.join(TODO_FOLDER, "config.json")

WELCOME = """
[b default on cyan3]     [/] │ A Todo   
[b default on cyan3]  TD [/] │ Command Line Tool

[b]欢迎使用 [cyan3]todo-cmd[/][b] 命令行工具！
这是一个简单的工具，可以帮助你管理待办事项。[/]

Welcome to the [b cyan3]todo-cmd[/]!
This is a simple tool to help you manage your tasks.
"""

TRANS = {
    "created_todo_folder": {
        "en": "Created todo storage folder at ~./todo",
        "zh": "已创建todo文件存储路径 ~/.todo"
    },
    "created_todo_json": {
        "en": "Created todo file at ~/.todo/todo.json",
        "zh": "已创建todo文件 ~/.todo/todo.json"
    },
    "created_config": {
        "en": "Created config: ~/.todo/config.json",
        "zh": "已创建config文件 ~/.todo/config.json"
    },
    "is_overwrite_todo": {
        "en": "todo.json is already exists, overwrite or not",
        "zh": "todo.json 已存在，是否覆盖原有文件"
    },
    "init_done": {
        "en": "Configuration Initialized",
        "zh": "配置初始化完成"
    }
}

def main():
    """Greet the user and perform initial setup."""
    # welcome
    t.console.print(WELCOME)

    # setting config
    lang = t.ask(
        "请选择语言 | Please select language", 
        choices=["zh", "en"],
        default="zh"
    )

    # create local folder
    if not os.path.exists(TODO_FOLDER):
        os.mkdir(TODO_FOLDER)
        t.done(TRANS["created_todo_folder"][lang])

    # create todo.json file
    is_create_todo_json = True
    if os.path.exists(TODO_FILE):
        # already has todo.json file
        is_create_todo_json = Confirm.ask(
            t.ASK_MARK + " " + TRANS["is_overwrite_todo"][lang],
            default=False
        )
    
    if is_create_todo_json:
        with open(TODO_FILE, "w") as fp:
            json.dump([], fp)
        t.done(TRANS["created_todo_json"][lang])
    
    # create config file
    config_dict = {
        "language": lang,
        "ddl_delta": 3  # delay on day
    }
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as fp:
            json.dump(config_dict, fp, indent=2)
        t.done(TRANS["created_config"][lang])

    t.done(TRANS["init_done"][lang])


if __name__ == '__main__':
    main()
