import rich_click as click
from rich.console import Console

from todo_cmd.sub_cmd.init_todo import main as init_todo
from todo_cmd.sub_cmd.todo_add import add
from todo_cmd.sub_cmd.todo_ls import ls
from todo_cmd.sub_cmd.todo_log import log
from todo_cmd.sub_cmd.todo_rm import rm


console = Console()


@click.group()
def todo():
    pass


def main():
    # todo.add_command(init_todo, "init")
    todo.add_command(add)
    todo.add_command(ls)
    todo.add_command(log)
    todo.add_command(rm)
    todo()


if __name__ == "__main__":
    main()
