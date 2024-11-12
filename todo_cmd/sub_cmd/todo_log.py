"""Add a finished task as log"""
import datetime

import rich_click as click

import todo_cmd.templates as t
from todo_cmd.language import TRANS
from todo_cmd.interface.todo import todo_interface
from todo_cmd.interface.task import Task


@click.command()
@click.argument("task", nargs=-1)
def log(task: str):
    """新建日志 | Add a log"""
    # check if task is empty
    task = " ".join(task)
    if len(task.strip()) == 0:
        t.error(TRANS("log_should_not_be_empty"))
        exit(1)

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
    t.info(f"{TRANS('new_task')}: <{next_id}> {task}")
    t.info(f"{TRANS('created_date')}: {log_date}")
