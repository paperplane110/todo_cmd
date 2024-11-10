"""
When the user first time uses `todo`,
init `config.json` and `todo.json` in ~/.todo/
"""
import os
import json

import rich_click as click
from rich.console import Console
from rich.prompt import Prompt, Confirm

import todo_cmd.templates as t
from todo_cmd.language import i2n

console = Console()

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

@click.command()
def main():
    """Greet the user and perform initial setup."""
    # welcome
    console.print(WELCOME)

    # setting config
    lang = Prompt.ask(
        t.question("请选择语言 | Please select language"),
        choices=["zh", "en"],
        default="zh"
    )

    # create local folder
    if not os.path.exists(TODO_FOLDER):
        os.mkdir(TODO_FOLDER)
        console.print(t.done(i2n("create_todo_folder", lang)))

    # create todo.json file
    is_create_todo_json = False
    if os.path.exists(TODO_FILE):
        # already has todo.json file
        is_create_todo_json = Confirm.ask(
            t.question("todo.json 已存在，是否覆盖原有文件"),
            default=False
        )
    
    if is_create_todo_json:
        with open(TODO_FILE, "w") as fp:
            json.dump([], fp)
        console.print(t.done(i2n("created_todo_json", lang)))
    
    # create config file
    config_dict = {
        "language": lang,
        "ddl_delta": 3600 * 12
    }
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as fp:
            json.dump(config_dict, fp, indent=2)
        console.print(t.done(i2n("created_config", lang)))

    console.print(t.done("初始化完成"))


if __name__ == '__main__':
    main()
