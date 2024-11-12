# Todo in Command Line

欢迎使用 todo-cmd，这是一个简单的工具，帮助您在命令行中轻松管理代办、记录完成事项。

## 1. 安装｜Installation

目前仅支持通过源码安装，需要 python3.7^

```shell
git clone https://github.com/paperplane110/todo_cmd.git
cd todo_cmd
pip3 install -e .
```

## 2. 使用方法｜Usage

### Add a todo task

```bash
todo add ${task}

# or use shortcut
todo a ${task}

# with deadline
todo add ${task} --deadline ${YYYYMMdd}
todo add ${task} -ddl ${YYYYMMdd}
```

### Add a finished task

```shell
todo log ${task}

# or use shortcut
todo l ${task}
```

### List tasks

List all tasks

```shell
todo ls
```

List tasks by given status (`todo`|`done`)

```shell
todo ls ${status}
```

### Set a Task Done

```shell
todo done ${task_id}
```

### Remove a Task

```shell
todo rm ${task_id}
```

### Modify a Task

```shell
todo mod ${task_id}

# or use shortcut
todo m ${task_id}
```

More options: [`todo mod`](./docs/todo_mod.md)

## 3. 开发者｜For Developer

Install todo_cmd in editable mode

```shell
pip install -e .
```

## 4.设计文档｜Design Documents

- [Task class](./docs/task_class.md)
  - [Task status](./docs/task_status.md)
- [Design of `todo rm`](./docs/todo_rm.md)
- [Design of `todo mod`](./docs/todo_mod.md)
