import datetime

import rich_click as click
from rich.prompt import Prompt
from rich.console import Console

import todo_cmd.templates as t
from todo_cmd.language import i2n
from todo_cmd.interface.config import CONFIG
from todo_cmd.interface.task import Task
from todo_cmd.interface.todo import todo_interface

# Load configuration
LANG = CONFIG["language"]
DDL_DELTA = int(CONFIG["ddl_delta"])

console = Console()



@click.command()
@click.argument("task")
@click.option("-ddl", "--deadline", default=None, help=i2n("help_ddl", LANG))
def add(task: str, deadline: datetime.datetime):
    """Add a task"""
    now_dt = datetime.datetime.now()
    now_str = now_dt.strftime("%Y-%m-%d_%H:%M:%S")
    
    if not deadline:
        # default ddl
        default_ddl_dt = now_dt + datetime.timedelta(seconds=DDL_DELTA)
        default_ddl_str = default_ddl_dt.strftime("%Y-%m-%d")

        console.print(t.info(f"Now: {now_str}"))
        deadline = Prompt.ask(
            t.question("Please specify a deadline"),
            default=default_ddl_str
        )

    # check input task
    if len(task.strip()) == 0:
        console.print(t.error(f"todo 内容不能为空"))
        exit(1)
    if " " in task:
        task = f"\"{task}\""

    next_id = todo_interface.max_id + 1
    task_obj = Task(
        task=task,
        task_id=next_id,
        ddl=deadline,
        status="todo"
    )
    todo_interface.add_todo(task_obj)
    console.print(t.info(f"新建任务：{next_id}|{task}"))
    console.print(t.info(f"创建日期：{now_str}"))
    console.print(t.info(f"截止日期：{deadline}"))
