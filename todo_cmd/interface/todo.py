import os
import json
from typing import List, Optional

from todo_cmd.sub_cmd.init_todo import main as init_todo
from todo_cmd.interface.task import (
    Task,
    task_list_serializer,
    task_list_deserializer
)


class TodoInterface:
    todo_folder = os.path.join(os.path.expanduser('~'), '.todo')
    todo_file = os.path.join(todo_folder, 'todo.json')

    def __init__(self):
        self.max_id = -1
        self.todo_list = self.read_todo()

    def read_todo(self) -> List[Task]:
        """read local todo file

        Returns:
            List[Task]: a list of task
        """
        # First time use, todos not exists
        if not os.path.exists(self.todo_file):
            init_todo()
            return []
        
        with open(self.todo_file, "r") as fp:
            raw_list = json.load(fp)
        todo_list = task_list_deserializer(raw_list)
        if len(todo_list) != 0:
            self.max_id = max(todo_list, key=lambda task: int(task.task_id)).task_id

        return todo_list

    def save_todos(self, todo_list: List[Task]):
        """Save task list to disk"""
        with open(self.todo_file, "w") as fp:
            json.dump(
                todo_list,
                fp,
                default=task_list_serializer,
                indent=2
            )

    def add_todo(self, task: Task) -> bool:
        """add task to todo and save to disk"""
        self.todo_list.append(task)
        self.save_todos(self.todo_list)
        self.max_id += 1

    def find_by_id(self, req_id: int) -> Optional[Task]:
        """find task by id"""
        if req_id > self.max_id:
            return None
        if req_id < 0:
            return None
        for task in self.todo_list:
            if task.task_id == req_id:
                return task
        return None
    
    def remove_task(self, req_id: int) -> Optional[Task]:
        """remove task from todo list"""
        is_found = False
        for idx, task in enumerate(self.todo_list):
            if task.task_id == req_id:
                is_found = True
                break
        if is_found:
            task = self.todo_list.pop(idx)
            self.save_todos(self.todo_list)
        else:
            task = None
        return task

todo_interface = TodoInterface()
