"""Modify a task"""
from typing import Tuple
from datetime import datetime
# import readline

import rich_click as click
from rich.prompt import Prompt

import todo_cmd.templates as t
from todo_cmd.validation import val_ddl_callback
from todo_cmd.interface.todo import todo_interface
from todo_cmd.interface.task import TASK_STATUS, Task
from todo_cmd.language import TRANS


@click.command()
@click.argument("id", type=int)
@click.option("-t", "--task", "task_des", 
              type=str, default=None, help=TRANS("mod_help_task"))
@click.option("-s", "--status", 
              type=click.Choice(["todo", "done"]), 
              help=TRANS("mod_help_status"))
@click.option("-ddl", "--ddl",
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
    if not task:
        t.error(f"{TRANS('task_not_found')}, id: {id}")
        exit(1)

    # User only provides id, ask one by one
    if (task_des is None) and (status is None) and (ddl is None):
        # ask new task
        task_des = t.ask(TRANS("task"), default=task.task)
        task.task = task_des
        status = t.ask(TRANS("status"), default=task.status)
        if not task.update_status(status):
            t.error("update_status_failed")
        ddl = t.ask(TRANS("ddl"), default=task.ddl)
        task.ddl = ddl
        todo_interface.save_todos()
        t.done(TRANS("mod_success"))
        return 0
    
    # User provides some options
    if task_des:
        task.task = task_des

    if status:
        if not task.update_status(status):
            t.error("update_status_failed")
    
    if ddl:
        task.ddl = ddl

    todo_interface.save_todos()
    t.done(TRANS("mod_success"))
