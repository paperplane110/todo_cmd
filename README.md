# Todos in Command Line

欢迎使用 todo-cmd，这是一个简单的工具，帮助您在命令行中轻松管理代办、记录完成事项。

## Add a todo task

```bash
todo add ${task}

# with deadline
todo add ${task} --deadline ${YYYYMMdd}
todo add ${task} -ddl ${YYYYMMdd}
```

## Add a finished task

```shell
todo log ${task}
```

## List tasks

List tasks of `todo` status

```shell
todo ls
```

List all tasks

```shell
todo ls -a
todo ls --all
```

List tasks by given status (`todo`|`done`)

```shell
todo ls ${status}
```

## Set a Task Done

```shell
todo done ${task_id}
```

## Remove a Task

```shell
todo rm ${task_id}
```

## Modify a Task

```shell
todo mod ${task_id}
```

## Developer

Install todo_cmd editable

```shell
pip install -e .
```

## Design Documents

- [Task class](./docs/task_class.md)
- [Task status](./docs/task_status.md)
