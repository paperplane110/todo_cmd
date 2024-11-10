import datetime

import rich_click as click
from rich.console import Console

import todo_cmd.templates as t
from todo_cmd.language import i2n
from todo_cmd.interface.config import CONFIG
from todo_cmd.interface.todo import todo_interface
from todo_cmd.interface.task import Task

# Load configuration
lang = CONFIG["language"]

console = Console()


@click.command()
@click.argument("task", nargs=-1)
def log(task: str):
    """Add a log"""
    # check if task is empty
    task = " ".join(task)
    if len(task.strip()) == 0:
        console.print(t.error(f"log 内容不能为空"))
        exit(1)
    if " " in task:
        task = f"\"{task}\""

    log_date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    next_id = todo_interface.max_id + 1
    task_obj = Task(
        task=task,
        task_id=next_id,
        created_date=log_date,
        ddl=log_date,
        status="done",
        done_date=log_date
    )
    todo_interface.add_todo(task_obj)
    console.print(t.info(f"新建日志：{next_id}|{task}"))
    console.print(t.info(f"创建日期：{log_date}"))
