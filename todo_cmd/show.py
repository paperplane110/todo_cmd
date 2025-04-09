"""Show tasks"""
from typing import List, Tuple, Literal, Optional
from datetime import datetime

from rich.table import Table

import todo_cmd.templates as t
from todo_cmd.language import TRANS
from todo_cmd.interface.task import Task, TASK_PRIORITY
from todo_cmd.validation import val_date_fmt


ExprList = List[Task]
TodoList = List[Task]
DoneList = List[Task]
DiscardList = List[Task]
TaskLabel = Literal["expr", "todo", "done"]


def classify_tasks(
        task_list: List[Task]
    ) -> Tuple[ExprList, TodoList, DoneList, DiscardList]:
    """classify task list into three list: expr, todo, done

    Args:
        task_list (List[Task]): task list
    """
    over_due_list = list(filter(
        lambda task: task.is_over_due, 
        task_list
    ))
    todo_list = list(filter(
        lambda task: task.is_strict_todo, 
        task_list
    ))
    done_list = list(filter(
        lambda task: task.is_done, 
        task_list
    ))
    discard_list = list(filter(
        lambda task: task.is_discard,
        task_list
    ))
    return (over_due_list, todo_list, done_list, discard_list)


def summary(task_list: List[Task]):
    expr, todo, done, discard = classify_tasks(task_list)
    t.info(f"{TRANS('total_tasks')}: {len(task_list)}")
    t.error(f"{TRANS('overdue_tasks')}: {len(expr)}")
    t.todo(f"{TRANS('todo_tasks')}: {len(todo)}")
    t.done(f"{TRANS('done_tasks')}: {len(done)}")
    t.discard(f"{TRANS('discard_tasks')}: {len(discard)}")


def simplify_date(date_str: str) -> str:
    dt = val_date_fmt(date_str)
    if not dt:
        # empty or invalid date
        return "/"
    return dt.strftime("%Y-%m-%d")


def label_priority(priority: TASK_PRIORITY):
    """convert plain priority string to colored label

    Args:
        priority (str): p0, p1, p2, p3
    """
    if priority == "p0":
        return t.red_label(priority)
    elif priority == "p1":
        return t.orange_label(priority)
    elif priority == "p2":
        return t.green_label(priority)
    else:
        return t.gray_label(priority)


def table(task_list: List[Task], verbose: bool=False):
    """Display tasks table

    Args:
        task_list (List[Task]): task list
        verbose (bool, optional): show more info like created date. Defaults to False.
    """
    
    def add_section(
            table: Table, 
            t_list: List[Task], 
            t_label: TaskLabel, 
            verbose: bool=False
        ):
        """add section to table, will effect table object"""
        status_str = ""
        if t_label == "expr":
            status_str = t.red_label(TRANS(t_label))
        elif t_label == "todo":
            status_str = t.blue_label(TRANS(t_label))
        elif t_label == "done":
            status_str = t.green_label(TRANS(t_label))
        elif t_label == "discard":
            status_str = t.gray_label(TRANS(t_label))

        for idx, task in enumerate(t_list):
            is_last_elem = True if (idx+1) == len(t_list) else False
            if not verbose:
                table.add_row(
                    str(task.task_id),
                    status_str,
                    label_priority(task.priority),
                    task.task,
                    simplify_date(task.ddl),
                    simplify_date(task.done_date),
                    end_section=is_last_elem
                )
            else:
                table.add_row(
                    str(task.task_id),
                    status_str,
                    label_priority(task.priority),
                    task.task,
                    task.ddl,
                    task.created_date,
                    task.done_date,
                    end_section=is_last_elem
                )

    # Some filter logic
    over_due_list, todo_list, done_list, discard_list = classify_tasks(task_list)

    # Some sort logic
    # default: sort tasks by status
    for l in [todo_list, over_due_list, done_list, discard_list]:
        l.sort(key=lambda task: task.created_date, reverse=True)

    table = Table()
    table.add_column("id", style="cyan", no_wrap=True)
    table.add_column(TRANS("status"), no_wrap=True)
    table.add_column(TRANS("priority"), no_wrap=True)
    table.add_column(TRANS("task"), style="magenta")
    table.add_column(TRANS("ddl"), justify="center")
    if verbose:
        table.add_column(TRANS("created_date"), justify="center")
    table.add_column(TRANS("finish_date"), justify="center")

    add_section(table, over_due_list, "expr", verbose)
    add_section(table, todo_list, "todo", verbose)
    add_section(table, done_list, "done", verbose)
    add_section(table, discard_list, "discard", verbose)
    t.console.print(table)
