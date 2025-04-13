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
from datetime import datetime, timedelta
from typing import List, Literal, Union, Tuple, Optional

import rich_click as click

import todo_cmd.templates as t
import todo_cmd.show as show 
from todo_cmd.language import TRANS
from todo_cmd.validation import val_date_fmt_callback, val_date_fmt
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
FilterStatusType = Literal["todo", "done", "expr"]

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


OperatorType = Literal["gt", "lt"]
def filter_compare_date(
        input_dt: datetime,
        task_list: List[Task],
        operator: OperatorType = "gt",
        compare_attr: str="created_date"
    ) -> List[Task]:
    res_list = []
    for task in task_list:
        task_dt = val_date_fmt(getattr(task, compare_attr))
        if not task_dt:
            continue
        if operator == "gt":
            if task_dt > input_dt:
                res_list.append(task)
        else:
            if task_dt <= input_dt:
                res_list.append(task)
    return res_list


# @deprecated
def find_tasks_by_time_range(time_range: TimeRangeType, task_list: List[Task]):
    task_list = todo_interface.task_list
    if time_range == "t" or time_range == "today":
        today = datetime.now().strftime("%Y-%m-%d")
        today_dt = datetime.strptime(today, "%Y-%m-%d")
        tmr_dt = today_dt + timedelta(days=1)
        task_list = filter_compare_date(today_dt, task_list, "gt")
        task_list = filter_compare_date(tmr_dt, task_list, "lt")
    elif time_range == "yest" or time_range == "yesterday":
        ...
    elif time_range == "w" or time_range == "week":
        ...
    elif time_range == "m" or time_range == "month":
        ...
    elif time_range == "y" or time_range == "year":
        ...
    

def check_status_flag(todo: bool, done: bool, expr: bool) -> Optional[FilterStatusType]:
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
        

def check_start_end_option(start: datetime, end: datetime):
    if start and end:
        if start > end:
            t.error(f"start: {start}")
            t.error(f"end  : {end}")
            t.error(TRANS("end_should_later_than_start"))
            exit(1)


# [Bug]? discard status is missing
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
        task_list = todo_interface.task_list
    check_start_end_option(start, end)
    status_flag = check_status_flag(is_show_todo,is_show_done, is_show_expr)

    # 没有任何输入：展示全部
    # 有 args:ids 限制，可以经过时间范围、任务状态过滤
    # 有 args:time_range 限制，不经过时间范围，要经过任务状态
    # 无 args，有时间范围，可经过任务状态筛选
    # 也就是说，任务筛选无论如何都要经过
    if (input_args is None) and (start or end):
        # args 未确定时间范围，用户通过 start end 参数确定了时间
        if start:
            # 筛选 create and done 日期大于 start 的任务
            task_list_created_after_start = filter_compare_date(start, task_list, "gt")
            task_list_done_after_start = filter_compare_date(start, task_list, "gt", "done_date")
            task_list = list(set(task_list_created_after_start + task_list_done_after_start))
        if end:
            # 筛选 create and done 日期小于 end 的任务
            task_list_created_before_end = filter_compare_date(end, task_list, "lt")
            task_list_done_before_end = filter_compare_date(end, task_list, "lt", "done_date")
            task_list = list(set(task_list_created_before_end + task_list_done_before_end))

    if status_flag:
        # just filter with status
        if status_flag == "todo":
            task_list = list(filter(lambda task: task.status == "todo", task_list))
        if status_flag == "done":
            task_list = list(filter(lambda task: task.status == "done", task_list))
        if status_flag == "expr":
            task_list = list(filter(
                lambda task: task.is_over_due,
                task_list
            ))

    if len(task_list) == 0:
        t.info(TRANS("task_not_found"))
        return 0
    
    show.table(task_list, verbose)
    show.summary(task_list)
    