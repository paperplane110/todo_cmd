import rich_click as click
from rich.console import Console

from todo_cmd.sub_cmd.todo_add import add
from todo_cmd.sub_cmd.todo_ls import ls


console = Console()


@click.group()
def todo():
    pass


def main():
    todo.add_command(add)
    todo.add_command(ls)
    todo()


if __name__ == "__main__":
    main()
