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
from typing import List, Literal, Union, Tuple

import rich_click as click
from rich.table import Table

import todo_cmd.templates as t
import todo_cmd.show as show 
from todo_cmd.language import TRANS
from todo_cmd.validation import val_date_fmt_callback
from todo_cmd.interface.todo import todo_interface
from todo_cmd.interface.task import Task

TIME_RANGE = (
    # histroy
    "t", "today",
    "yest", "yesterday",
    "w", "week",
    "m", "month",
    "y", "year",
    # future
    "tmr", "tomorrow",
    "nw", "next week",
    "nm", "next month",
    "ny", "next year"
)
"""Args support time range"""

TimeRangeType = Literal[
    # histroy
    "t", "today",
    "yest", "yesterday",
    "w", "week",
    "m", "month",
    "y", "year",
    # future
    "tmr", "tomorrow",
    "nw", "next week",
    "nm", "next month",
    "ny", "next year"
]
ArgsType = Literal["ids", "time_range", "none"]
ProcessedArgsType = Union[List[int], TimeRangeType, None]


def check_args(args: tuple) -> Tuple[ArgsType, ProcessedArgsType]:
    """Check args input, There are three situations

    - a list ids: return ("ids", a list of ids)
    - a word for time range: return ("time_range", args_str)
    - empty input: ("none", None)
    """
    res = None
    # if has args, ignore other options
    if len(args):
        # pick first arg, check its type, int or str
        first_arg: str = args[0]
        if first_arg.isdigit():
            # should be a int list
            res = []
            for arg in args:
                try:
                    res.append(int(arg))
                except ValueError:
                    t.warn(f"arg not int: {arg}")
            res = set(res)
            return ("ids", res)
            
        else:
            args_str = " ".join(args)
            if args_str not in TIME_RANGE:
                t.error(f"Unsupport arg {args_str}, please input valid word: {TIME_RANGE}")
            else:
                return ("time_range", args_str)
    return ("none", res)


def find_tasks_by_ids(ids: List[int], task_list: List[Task]):
    """find task by ids, and append tasks to task_list
    Will side-effect task_list
    """
    missing_list = []
    for _id in ids:
        found_task = todo_interface.find_by_id(_id)
        if found_task:
            task_list.append(found_task)
        else:
            missing_list.append(_id)
    if len(missing_list) != 0:
        t.warn(f"task {missing_list} not found")


def find_tasks_by_time_range(time_range: TimeRangeType, task_list: List[Task]):
    if time_range == "t" or time_range == "today":
        ...
    elif time_range == "yest" or time_range == "yesterday":
        ...
    elif time_range == "w" or time_range == "week":
        ...
    elif time_range == "m" or time_range == "month":
        ...
    elif time_range == "y" or time_range == "year":
        ...
    

def check_status_flag(todo: bool, done: bool, expr: bool) -> str:
    """check input flag, only output one

    Args:
        todo (bool): is show todo
        done (bool): is show done
        expr (bool): is show expr

    Returns:
        str: 
    """
    if (todo and done) or (todo and expr) or (done and expr):
        t.error("Please only input one flag, either todo/done/expr")
        return None
    if not (todo or done or expr):
        # all false
        return None
    if todo:
        return "todo"
    elif done:
        return "done"
    else:
        return "expr"
    

@click.command()
@click.argument("args", nargs=-1)
@click.option("-s", "--start", callback=val_date_fmt_callback)
@click.option("-e", "--end", callback=val_date_fmt_callback)
@click.option("-t", "--todo", "is_show_todo", is_flag=True)
@click.option("-d", "--done", "is_show_done", is_flag=True)
@click.option("-ex", "--expr", "is_show_expr", is_flag=True)
@click.option("-v", "--verbose", is_flag=True)
def ls(
    args: tuple, 
    start: datetime,
    end: datetime,
    is_show_todo: bool, 
    is_show_done: bool,
    is_show_expr: bool,
    verbose: bool
):
    """展示任务 | Show all tasks"""
    task_list = []
    args_type, input_args = check_args(args)
    if args_type == "ids":
        find_tasks_by_ids(input_args, task_list)
    elif args_type == "time_range":
        find_tasks_by_time_range(input_args, task_list)
    else:
        pass
    status_flag = check_status_flag(is_show_todo, is_show_expr, is_show_done)

    if input_args is None and status_flag is None:
        task_list = todo_interface.task_list

    if len(task_list) == 0:
        t.info(TRANS("task_not_found"))
        return 0
    
    show.table(task_list, verbose)
    show.summary(task_list)
    