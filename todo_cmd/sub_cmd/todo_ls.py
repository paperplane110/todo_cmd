"""List tasks
TODO: Implement better tui
TODO: Sort
    - by status
    - by created_date
    - by done_date
    - by ddl
TODO: add more filter methods
    - status
    - date
"""
import datetime

import rich_click as click
from rich.console import Console
from rich.table import Table

import todo_cmd.templates as t
from todo_cmd.interface.todo import todo_interface
from todo_cmd.interface.task import Task

console = Console()


def get_status_str(task: Task) -> str:
    now_dt = datetime.datetime.now()
    return task.status


@click.command()
@click.option("-a", "--all", is_flag=True)
def ls(all: bool):
    """Show all tasks"""
    task_list = todo_interface.todo_list
    if len(task_list) == 0:
        console.print(t.info("No tasks in todo list"))
        return 0
    
    # Some filter logic
    todo_list = list(filter(lambda task: task.status=="todo", task_list))

    # Some sort logic
    task_list.sort(key=lambda task: task.status, reverse=True)    # default: sort tasks by status

    table = Table(
        show_lines=True
    )
    table.add_column("id", style="cyan", no_wrap=True)
    table.add_column("status", no_wrap=True)
    table.add_column("task", style="magenta")
    table.add_column("ddl", justify="center")
    table.add_column("done_date", justify="center")

    for task in task_list:
        status_str = get_status_str(task)
        table.add_row(
            str(task.task_id),
            status_str,
            task.task,
            task.ddl,
            task.done_date
        )
    console.print(table)
    console.print(t.info(f"总计任务数: {len(task_list)}"))
    console.print(t.info(f"待完成个数: {len(todo_list)}"))
