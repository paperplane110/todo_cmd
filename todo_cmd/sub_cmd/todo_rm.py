"""Remove a task"""
import rich_click as click
from rich.console import Console
from rich.prompt import Confirm

import todo_cmd.templates as t
from todo_cmd.language import TRANS
from todo_cmd.interface.todo import todo_interface

console = Console()


@click.command()
@click.argument("id", type=int)
def rm(id: int): 
    """删除任务 | Remove a task by given id"""
    # is id valid?
    task = todo_interface.find_by_id(id)
    if not task:
        console.print(t.error(f"{TRANS('task_not_found')}, id: {id}"))
        exit(1)

    is_rm = Confirm.ask(
        t.question(f"{TRANS('is_rm_task')}: {id}"),
        default=False
    )

    if is_rm:
        drop_task = todo_interface.remove_task(id)
        if drop_task:
            console.print(t.done(f"{TRANS('done_rm_task')}, {drop_task}"))
        else:
            console.print(t.error(f"{TRANS('task_not_found')}, id: {id}"))
            exit(1)
