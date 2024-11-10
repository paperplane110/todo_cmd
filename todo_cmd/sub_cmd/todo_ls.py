import rich_click as click
from rich.console import Console

import todo_cmd.templates as t
from todo_cmd.interface.todo import todo_interface

console = Console()

@click.command()
def ls():
    """Show all tasks"""
    task_list = todo_interface.todo_list
    if len(task_list) == 0:
        console.print(t.info("No tasks in todo list"))
        return 0

    console.print(task_list)