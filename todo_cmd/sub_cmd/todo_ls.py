"""List tasks
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
from rich.table import Table

import todo_cmd.templates as t
from todo_cmd.language import TRANS
from todo_cmd.validation import val_date_fmt
from todo_cmd.interface.todo import todo_interface
from todo_cmd.interface.task import Task


def is_over_due(task: Task) -> bool:
    # For tasks already done, its not over due
    if task.status == "done":
        return False
    # get ddl datetime
    ddl_dt = val_date_fmt(task.ddl)

    now_dt = datetime.datetime.now()
    if (now_dt < ddl_dt):
        return False
    else:
        return True


@click.command()
@click.option("-a", "--all", is_flag=True)
def ls(all: bool):
    """展示任务 | Show all tasks"""
    task_list = todo_interface.todo_list
    if len(task_list) == 0:
        t.info("No tasks in todo list")
        return 0
    
    # Some filter logic
    todo_list = list(filter(
        lambda task: (task.status=="todo") and (not is_over_due(task)), 
        task_list
    ))
    over_due_list = list(filter(
        lambda task: (task.status=="todo") and (is_over_due(task)), 
        task_list
    ))
    done_list = list(filter(lambda task: task.status=="done", task_list))

    todo_list_len = len(todo_list)
    over_due_list_len = len(over_due_list)
    done_list_len = len(done_list)

    # Some sort logic
    # default: sort tasks by status
    for l in [todo_list, over_due_list, done_list]:
        l.sort(key=lambda task: task.created_date, reverse=True)

    table = Table(
        # show_lines=True
    )
    table.add_column("id", style="cyan", no_wrap=True)
    table.add_column(TRANS("status"), no_wrap=True)
    table.add_column(TRANS("task"), style="magenta")
    table.add_column(TRANS("ddl"), justify="center")
    table.add_column(TRANS("finish_date"), justify="center")

    for idx, task in enumerate(over_due_list):
        status_str = f"[default on red3] {TRANS('expr')} [/]"
        is_last_elem = True if (idx+1) == over_due_list_len else False
        table.add_row(
            str(task.task_id),
            status_str,
            task.task,
            task.ddl,
            task.done_date,
            end_section=is_last_elem
        )
    for idx, task in enumerate(todo_list):
        status_str = f"[default on dodger_blue2] {TRANS('todo')} [/]"
        is_last_elem = True if (idx+1) == todo_list_len else False
        table.add_row(
            str(task.task_id),
            status_str,
            task.task,
            task.ddl,
            task.done_date,
            end_section=is_last_elem
        )
    for task in done_list:
        status_str = f"[default on green4] {TRANS('done')} [/]"
        table.add_row(
            str(task.task_id),
            status_str,
            task.task,
            task.ddl,
            task.done_date
        )
    t.console.print(table)
    t.info(f"{TRANS('total_tasks')}: {len(task_list)}")
    t.error(f"{TRANS('overdue_tasks')}: {over_due_list_len}")
    t.todo(f"{TRANS('todo_tasks')}: {todo_list_len}")
    t.done(f"{TRANS('done_tasks')}: {done_list_len}")
