import os

import rich_click as click
from rich.console import Console

from todo_cmd.sub_cmd.todo_add import add
from todo_cmd.sub_cmd.todo_ls import ls
from todo_cmd.sub_cmd.todo_log import log
from todo_cmd.sub_cmd.todo_rm import rm
from todo_cmd.sub_cmd.todo_mod import mod
from todo_cmd.sub_cmd.todo_done import done
from todo_cmd.sub_cmd.todo_discard import discard
from todo_cmd.sub_cmd.todo_config import config


if os.name == 'nt':
    try:
        import pyreadline
    except:
        print("readline is disabled in Windows. Please run: pip install pyreadline")
elif os.name == 'posix':
    import readline


console = Console()


@click.command(cls=click.RichGroup)
def todo():
    """欢迎使用 todo-cmd，这是一个简单的工具，帮助您在命令行中轻松管理代办、记录完成事项。
    
    \bWelcome to the todo-cmd! This is a simple tool to help you manage your tasks.
    """
    ...


def main():
    # todo.add_command(init_todo, "init")
    todo.add_command(add)
    todo.add_command(add, "a")

    todo.add_command(ls)

    todo.add_command(log)
    todo.add_command(log, "l")

    todo.add_command(rm)

    todo.add_command(mod)
    todo.add_command(mod, "m")

    todo.add_command(config)

    todo.add_command(done)
    
    todo.add_command(discard, "drop")

    todo()


if __name__ == "__main__":
    main()
