import datetime

import rich_click as click
from rich.console import Console

import todo_cmd.templates as t
from todo_cmd.language import i2n
from todo_cmd.config_interface import read_config
from todo_cmd.task_interface import (
    Task,
    read_todos,
    save_todos
)

# Load configuration
conf = read_config()
lang = conf["language"]

console = Console()

@click.command()
@click.argument("task")
@click.option("-ddl", "--deadline", prompt=True, help=i2n("help_ddl", lang))
def add(task: str, deadline: datetime.datetime):
    """Add a task"""
    if " " in task:
        task = f"\"{task}\""
    created_date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    todos = read_todos()
    todos.append(Task(
        created_date=created_date,
        task=task,
        ddl=deadline,
        status="todo"
    ))
    console.print(t.info(f"新建任务：{task}"))
    console.print(t.info(f"创建日期：{created_date}"))
    console.print(t.info(f"截止日期：{deadline}"))
    save_todos(todos)