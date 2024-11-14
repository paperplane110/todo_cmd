"""Remove a task"""
from typing import Tuple

import rich_click as click
from rich.console import Console
from rich.prompt import Confirm

import todo_cmd.templates as t
from todo_cmd.language import TRANS
from todo_cmd.interface.todo import todo_interface

console = Console()


@click.command()
@click.argument("ids", nargs=-1)
def rm(ids: Tuple[int]): 
    """删除任务 | Remove a task by given id"""
    # is ids valid?
    ids_int_list = [int(id) for id in ids]
    for id in ids_int_list:
        task = todo_interface.find_by_id(id)
        if not task:
            console.print(t.error(f"{TRANS('task_not_found')}, id: {id}"))
            exit(1)

    if len(ids) == 0:
        t.error(TRANS("rm_task_is_empty"))
        return 0
    elif len(ids) == 1:
        # only remove one, won't ask for confirmation
        is_rm = True
    else:
        is_rm = Confirm.ask(
            f"{t.ASK_MARK} {TRANS('is_rm_task')}: {ids_int_list}",
            default=False
        )

    if is_rm:
        for id in ids_int_list:
            drop_task = todo_interface.remove_task(id)
            if drop_task:
                t.done(f"{TRANS('done_rm_task')}, {drop_task}")
            else:
                console.print(t.error(f"{TRANS('task_not_found')}, id: {id}"))
                exit(1)
