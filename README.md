```
                                                   __
 __________  ____  ____        _________ ___  ____/ /
/_  __/ __ \/ __ \/ __ \______/ ___/ __ `__ \/ __  / 
 / / / /_/ / /_/ / /_/ /_____/ /__/ / / / / / /_/ /  
/_/  \____/_____/\____/      \___/_/ /_/ /_/\__,_/   
                         
```

欢迎使用 **todo-cmd**，这是一个简单的工具，帮助您在命令行中轻松管理代办、记录完成事项。

Welcome to the **todo-cmd**!
This is a simple tool to help you manage your tasks.

## 1. 安装｜Installation

目前仅支持通过源码安装，需要 python3.8^

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
```txt
┏━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ id ┃ Status ┃ Task                                 ┃  Deadline  ┃ Finish Date ┃
┡━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 10 │  expr  │ Apply a card for my electric-bike    │ 2024-11-10 │      /      │
├────┼────────┼──────────────────────────────────────┼────────────┼─────────────┤
│ 9  │  todo  │ ask Liuke about perf monitor scripts │ 2024-11-13 │      /      │
├────┼────────┼──────────────────────────────────────┼────────────┼─────────────┤
│ 8  │  done  │ start a pr in rich                   │ 2024-11-12 │ 2024-11-12  │
│ 7  │  done  │ refactor template and ask            │ 2024-11-12 │ 2024-11-11  │
│ 6  │  done  │ find ICBC card                       │ 2024-11-12 │ 2024-11-12  │
│ 4  │  done  │ finish todo rm                       │ 2024-11-10 │ 2024-11-10  │
│ 3  │  done  │ go to ICBC update ID info            │ 2024-11-12 │ 2024-11-12  │
│ 1  │  done  │ add some translation                 │ 2024-11-10 │ 2024-11-10  │
└────┴────────┴──────────────────────────────────────┴────────────┴─────────────┘
```

List tasks by given status (`todo`|`done`|`expr`)

```shell
todo ls --${status}
```

More options: [`todo ls`](./docs/todo_ls.md)

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

### [Configuration](./docs/todo_config.md)

## 3. 开发者｜For Developer

Install todo_cmd in editable mode

```shell
pip install -e .
```

## 4.设计文档｜Design Documents

- [Task class](./docs/task_class.md)
  - [Task status](./docs/task_status.md)
- [Design of `todo ls`](./docs/todo_ls.md)
- [Design of `todo rm`](./docs/todo_rm.md)
- [Design of `todo mod`](./docs/todo_mod.md)
