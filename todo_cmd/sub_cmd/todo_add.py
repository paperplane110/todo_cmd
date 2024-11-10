"""Add a new task"""
import datetime
import readline

import rich_click as click
from rich.prompt import Prompt
from rich.console import Console

import todo_cmd.templates as t
from todo_cmd.language import TRANS
from todo_cmd.utils import validate_date_format
from todo_cmd.interface.config import CONFIG
from todo_cmd.interface.task import Task
from todo_cmd.interface.todo import todo_interface

# Load configuration
DDL_DELTA = int(CONFIG["ddl_delta"])

console = Console()



@click.command()
@click.argument("task", nargs=-1)
@click.option("-ddl", "--deadline", default=None, help=TRANS("help_ddl"))
def add(task: str, deadline: str):
    """新建任务 | Add a task"""
    # check input task
    task = " ".join(task)
    if len(task.strip()) == 0:
        console.print(t.error(f"todo 内容不能为空"))
        exit(1)
    console.print(t.info(f"{TRANS('new_task')}: {task}"))

    now_dt = datetime.datetime.now()
    now_str = now_dt.strftime("%Y-%m-%d_%H:%M:%S")
    
    if not deadline:
        # default ddl
        default_ddl_dt = now_dt + datetime.timedelta(seconds=DDL_DELTA)
        default_ddl_str = default_ddl_dt.strftime("%Y-%m-%d_%H:%M:%S")

        console.print(t.info(f"{TRANS('now')}: {now_str}"))
        deadline = Prompt.ask(
            t.question("Please specify a deadline"),
            default=default_ddl_str
        )

    ddl_dt = validate_date_format(deadline)
    deadline = ddl_dt.strftime("%Y-%m-%d_%H:%M:%S")

    

    next_id = todo_interface.max_id + 1
    task_obj = Task(
        task=task,
        task_id=next_id,
        ddl=deadline,
        status="todo"
    )
    todo_interface.add_todo(task_obj)
    console.print(t.info(f"{TRANS('new_task')}: {next_id} | {task}"))
    console.print(t.info(f"{TRANS('created_date')}: {now_str}"))
    console.print(t.info(f"{TRANS('ddl')}: {deadline}"))
