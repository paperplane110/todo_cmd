import os
import json
from typing import List, Optional

from todo_cmd.sub_cmd.init_todo import main as init_todo
from todo_cmd.interface.task import (
    Task,
    TASK_STATUS,
    task_list_serializer,
    task_list_deserializer
)


class TodoInterface:
    todo_folder = os.path.join(os.path.expanduser('~'), '.todo')
    todo_file = os.path.join(todo_folder, 'todo.json')

    def __init__(self):
        self.max_id = -1
        self.task_list = self.read_todo()

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

    def save_todos(self):
        """Save task list to disk"""
        with open(self.todo_file, "w") as fp:
            json.dump(
                self.task_list,
                fp,
                default=task_list_serializer,
                indent=2
            )

    def add_todo(self, task: Task) -> bool:
        """add task to todo and save to disk"""
        self.task_list.append(task)
        self.save_todos()
        self.max_id += 1

    def find_by_id(self, req_id: int) -> Optional[Task]:
        """find task by id"""
        if req_id > self.max_id:
            return None
        if req_id < 0:
            return None
        for task in self.task_list:
            if task.task_id == req_id:
                return task
        return None
    
    def find_tasks_by_status(self, status: TASK_STATUS) -> List[Task]:
        res_list = list(filter(
            lambda task: task.status == status, 
            self.task_list
        ))
        return res_list
    
    def remove_task(self, req_id: int) -> Optional[Task]:
        """remove task from todo list"""
        is_found = False
        for idx, task in enumerate(self.task_list):
            if task.task_id == req_id:
                is_found = True
                break
        if is_found:
            task = self.task_list.pop(idx)
            self.save_todos()
        else:
            task = None
        return task
    
    def update_status_by_id(self, req_id: int) -> Optional[Task]:
        """update the status of the task, which's id is req_id"""
        task = self.find_by_id(req_id)
        if not task:
            return None
        if not task.update_status("done"):
            return None
        self.save_todos()
        return task


todo_interface = TodoInterface()
