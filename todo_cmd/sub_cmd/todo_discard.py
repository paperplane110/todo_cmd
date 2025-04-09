"""Set a task's status to discard"""
from typing import Tuple

import rich_click as click

import todo_cmd.templates as t
from todo_cmd import show
from todo_cmd.language import TRANS
from todo_cmd.interface.todo import todo_interface

@click.command()
@click.argument("ids", nargs=-1, type=int)
def discard(ids:Tuple[int]):
    """丢弃任务 | Set the task to discard
    
    IDS could be one task id or multiple tasks' id
    """
    if len(ids) == 0:
        t.info(TRANS("please_input_task_id"))
        return 0
    
    invalid_ids = []
    valid_ids = []
    already_discarded_ids = []
    mod_success_task_list = []
    for id in ids:
        task = todo_interface.find_by_id(id)
        if task:
            if task.status == "discard":
                already_discarded_ids.append(id)
            else:
                task.update_status("discard")
                valid_ids.append(id)
                mod_success_task_list.append(task)
        else:
            invalid_ids.append(id)
    todo_interface.save_todos()

    if len(invalid_ids):
        t.error(f"{TRANS('task_not_found')}: {invalid_ids}")
    
    if len(already_discarded_ids):
        t.info(f"{TRANS('task_already_discarded')}: {already_discarded_ids}")

    if len(valid_ids):
        show.table(mod_success_task_list)
        t.done(f"{TRANS('task_discarded')}: {valid_ids}")