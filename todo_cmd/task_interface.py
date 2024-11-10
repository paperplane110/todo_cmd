import os
import json
from typing import Literal, Optional, List

from todo_cmd.init_todo import main as init_todo

TODO_FOLDER = os.path.join(os.path.expanduser('~'), '.todo')
TODO_FILE = os.path.join(TODO_FOLDER, 'todo.json')


class Task:
    """Task class"""
    def __init__(
            self,
            created_date: str,
            task: str,
            ddl: str,
            status: Literal["todo", "done"] = "done",
            tags: List[str] = [],
        ):
        """Initialize a Task"""
        self.created_date = created_date
        self.task = task
        self.ddl = ddl
        self.status = status
        self.tags = tags
        
    def to_json(self) -> dict:
        """serialize the task to dict"""
        return {
            "created_date": self.created_date,
            "task": self.task,
            "ddl": self.ddl,
            "status": self.status,
            "tags": self.tags
        }
    
    def __repr__(self):
        return f"Task(created_date={self.created_date}, task={self.task}, \
status={self.status}, ddl:{self.ddl}, tags={self.tags})"


def task_list_serializer(obj) -> dict:
    """Serialize Task object while json.dump"""
    if isinstance(obj, Task):
        return obj.to_json()


def task_list_deserializer(raw_list: List[dict]) -> List[Task]:
    """Deserialize a list of dict to a list Task"""
    res = []
    for raw_dict in raw_list:
        res.append(Task(**raw_dict))
    return res

def read_todos() -> List[Task]:
    """read local todo file

    Returns:
        List[Task]: a list of task
    """
    # First time use, todos not exists
    if not os.path.exists(TODO_FILE):
        init_todo()
        return []
    
    with open(TODO_FILE, "r") as fp:
        raw_list = json.load(fp)
    todos_list = task_list_deserializer(raw_list)

    return todos_list


def save_todos(todo_list: List[Task]):
    """Save task list to disk"""
    with open(TODO_FILE, "w") as fp:
        json.dump(
            todo_list,
            fp,
            default=task_list_serializer,
            indent=2
        )
