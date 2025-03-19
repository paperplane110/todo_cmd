"""Modify a task"""
from datetime import datetime

import rich_click as click

import todo_cmd.templates as t
from todo_cmd import show
from todo_cmd.validation import val_date_fmt_callback
from todo_cmd.interface.todo import todo_interface
from todo_cmd.interface.task import TASK_STATUS
from todo_cmd.language import TRANS


@click.command()
@click.argument("id", type=int)
@click.option("-t", "--task", "task_des", 
              type=str, default=None, help=TRANS("mod_help_task"))
@click.option("-s", "--status", 
              type=click.Choice(["todo", "done"]), 
              help=TRANS("mod_help_status"))
@click.option("-ddl", "--ddl",
              callback=val_date_fmt_callback,
              help=TRANS("mod_help_ddl"))
@click.option(
    "-p", "--priority",
    type=str, default=None,
    help=TRANS("mod_help_priority")
)
def mod(
        id: int,
        task_des: str,
        status: TASK_STATUS,
        ddl: datetime,
        priority: str
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
    if (task_des is None) and \
        (status is None) and \
        (ddl is None) and \
        (priority is None):
        # ask new task
        task_des = t.ask(TRANS("task"), default=task.task)
        task.task = task_des

        status = t.ask(TRANS("status"), default=task.status)
        if not task.update_status(status):
            t.error("update_status_failed")

        ddl = t.ask(TRANS("ddl"), default=task.ddl)
        if not task.update_ddl(ddl):
            t.error(TRANS("date_fmt_not_support"))

        priority = t.ask(TRANS("ask_priority"), default=task.priority, choices=["p0", "p1", "p2", "p3"])
        task.priority = priority

        todo_interface.save_todos()
        show.table([task])
        t.done(TRANS("mod_success"))
        return 0
    
    # User provides some options
    if task_des:
        task.task = task_des

    if status:
        if not task.update_status(status):
            t.error("update_status_failed")
    
    if ddl:
        ddl_str = ddl.strftime("%Y-%m-%d_%H:%M:%S")
        task.update_ddl(ddl_str)

    if priority:
        if not priority.startswith("p"):
            t.error(TRANS("priority_invalid"))
            exit(1)
        task.priority = priority

    todo_interface.save_todos()
    show.table([task])
    t.done(TRANS("mod_success"))
