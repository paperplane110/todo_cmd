"""Add a new task"""
import datetime

import rich_click as click

import todo_cmd.templates as t
from todo_cmd import show
from todo_cmd.language import TRANS
from todo_cmd.validation import val_date_fmt_callback, val_date_fmt
from todo_cmd.interface.config import CONFIG
from todo_cmd.interface.task import Task
from todo_cmd.interface.todo import todo_interface

# Load configuration
DDL_DELTA = int(CONFIG["ddl_delta"]) * 24 * 60 * 60


@click.command()
@click.argument("task", nargs=-1)
@click.option(
    "-ddl", "--deadline", 
    default=None,
    callback=val_date_fmt_callback,
    help=TRANS("help_ddl"))
@click.option(
    "-p", "--priority",
    type=str,
    default=None,
    help=TRANS("help_priority")
)
def add(task: str, deadline: str, priority: str):
    """新建任务 | Add a task"""
    # check input task
    task = " ".join(task)
    if len(task.strip()) == 0:
        t.error(TRANS("task_should_not_be_empty"))
        exit(1)
    t.info(f"{TRANS('new_task')}: {task}")

    now_dt = datetime.datetime.now()
    now_str = now_dt.strftime("%Y-%m-%d_%H:%M:%S")
    
    if not deadline:
        # default ddl
        default_ddl_dt = now_dt + datetime.timedelta(seconds=DDL_DELTA)
        default_ddl_str = default_ddl_dt.strftime("%Y-%m-%d_%H:%M:%S")

        t.info(f"{TRANS('now')}: {now_str}")
        deadline = t.ask(TRANS("ddl"), default=default_ddl_str)

    ddl_dt = val_date_fmt(deadline)
    if not ddl_dt:
        t.error(TRANS("date_fmt_not_support"))
        exit(1)
    deadline = ddl_dt.strftime("%Y-%m-%d_%H:%M:%S")

    if priority is None:
        priority = t.ask(TRANS("ask_priority"), choices=["p0", "p1", "p2", "p3"])

    next_id = todo_interface.max_id + 1
    task_obj = Task(
        task=task,
        task_id=next_id,
        ddl=deadline,
        status="todo",
        priority=priority
    )
    todo_interface.add_todo(task_obj)
    t.done(TRANS("new_task"))
    show.table([task_obj])
    # t.info(f"{TRANS('new_task')}: {next_id} | {task}")
    # t.info(f"{TRANS('created_date')}: {now_str}")
    # t.info(f"{TRANS('ddl')}: {deadline}")
