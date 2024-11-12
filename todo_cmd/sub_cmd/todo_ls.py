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
from typing import List

import rich_click as click
from rich.table import Table

import todo_cmd.templates as t
import todo_cmd.show as show 
from todo_cmd.language import TRANS
from todo_cmd.validation import val_date_fmt
from todo_cmd.interface.todo import todo_interface
from todo_cmd.interface.task import Task



@click.command()
@click.option("-a", "--all", is_flag=True)
@click.option("-v", "--verbose", is_flag=True, default=False)
def ls(all: bool, verbose: bool):
    """展示任务 | Show all tasks"""
    task_list = todo_interface.todo_list
    if len(task_list) == 0:
        t.info(TRANS("task_not_found"))
        return 0
    
    show.table(task_list, verbose)
    show.summary(task_list)
    