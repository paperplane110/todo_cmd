import datetime
from typing import Literal, List

from todo_cmd.validation import val_date_fmt


TASK_STATUS = Literal["todo", "done"]
DATE_ATTR = Literal["ddl", "create_date", "done_date"]


class Task:
    """Task class"""
    def __init__(
            self,
            task: str,
            task_id: int,
            ddl: str,
            status: TASK_STATUS = "done",
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
    
    def update_status(self, new_status: TASK_STATUS) -> bool:
        if self.status == new_status:
            return True
        if (self.status == "done") and \
            (new_status == "todo") and \
            (self.done_date is not None):
            self.status = new_status
            self.done_date = None
            return True
        if (self.status == "todo") and \
            (new_status == "done") and \
            (self.done_date is None):
            self.status = new_status
            self.done_date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            return True

        # ? are there any other choices
        return False
    
    def __update_date(self, date_str: str, attr: DATE_ATTR) -> bool:
        """validate and update date attribute"""
        dt = val_date_fmt(date_str)
        if dt is None:
            return False
        dt_str = dt.strftime("%Y-%m-%d_%H:%M:%S")
        setattr(self, attr, dt_str)
        return True

    def update_ddl(self, date_str: str) -> bool:
        return self.__update_date(date_str, "ddl")
    
    def update_created_date(self, date_str: str) -> bool:
        return self.__update_date(date_str, "create_date")
    
    def update_done_date(self, date_str: str) -> bool:
        return self.__update_date(date_str, "done_date")


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
