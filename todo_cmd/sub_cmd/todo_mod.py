"""Modify a task"""
from typing import Tuple
from datetime import datetime
# import readline

import rich_click as click
from rich.prompt import Prompt

import todo_cmd.templates as t
from todo_cmd.utils import validate_date_format
from todo_cmd.interface.todo import todo_interface
from todo_cmd.interface.task import TASK_STATUS, Task
from todo_cmd.language import TRANS


def val_ddl_callback(ctx, param, value):
    if value is None:
        return None
    try:
        dt = validate_date_format(value)
    except:
        t.error(f"{TRANS('ddl')}: {value}")
        t.error(TRANS("date_fmt_not_support"))
        exit(1)

    if not dt:
        t.error(f"{TRANS('ddl')}: {value}")
        t.error(TRANS("date_fmt_not_support"))
        exit(1)

    return dt


@click.command()
@click.argument("id", type=int)
@click.option("--task", "task_des", type=str, default=None, help=TRANS("mod_help_task"))
@click.option("--status", 
              type=click.Choice(["todo", "done"]), 
              help=TRANS("mod_help_status"))
@click.option("--ddl",
              type=str,
              callback=val_ddl_callback,
              help=TRANS("mod_help_ddl"))
def mod(
        id: int,
        task_des: str,
        status: TASK_STATUS,
        ddl: str
    ):
    """修改任务 | Modify the task by given id"""
    # Is id valid?
    # This task is a reference, 
    # modify this will effect the same element
    # in todo_interface.todo_list
    task = todo_interface.find_by_id(id)
    print(task.done_date)
    if not task:
        t.error(f"{TRANS('task_not_found')}, id: {id}")
        exit(1)

    # User only provides id, ask one by one
    if not (task_des and status and ddl):
        # ask new task
        task_des = t.ask(TRANS("task"), default=task.task)
        task.task = task_des
        status = t.ask(TRANS("status"), default=task.status)
        if not task.update_status(status):
            t.error("")
        ddl = t.ask(TRANS("ddl"), default=task.ddl)
        task.ddl = ddl
        todo_interface.save_todos()
        t.done(TRANS("mod_success"))
        return 0
    

    