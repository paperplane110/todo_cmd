import rich_click as click
from rich.console import Console

from todo_cmd.task_interface import (
    read_todos,
    Task
)

console = Console()

@click.command()
def ls():
    """Show all tasks"""
    todos = read_todos()
    console.print(todos)