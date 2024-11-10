import hashlib
import datetime
from typing import Literal, List


class Task:
    """Task class"""
    def __init__(
            self,
            task: str,
            task_id: int,
            ddl: str,
            status: Literal["todo", "done"] = "done",
            created_date: str = None,
            done_date: str = None,
            tags: List[str] = [],
        ):
        """Initialize a Task"""
        if not created_date:
            self.created_date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        else:
            self.created_date = created_date
        
        self.task_id = task_id
        self.task = task
        self.ddl = ddl
        self.status = status
        self.done_date = done_date
        self.tags = tags
        
    def to_json(self) -> dict:
        """serialize the task to dict"""
        return {
            "task_id": self.task_id,
            "created_date": self.created_date,
            "task": self.task,
            "ddl": self.ddl,
            "status": self.status,
            "done_date": self.done_date,
            "tags": self.tags
        }
    
    def __repr__(self):
        return f"Task(id={self.task_id}, created_date={self.created_date}, task={self.task}, \
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
