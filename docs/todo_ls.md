# List todo

## List all tasks

Sorted by:

- status: expr, todo, done
- created_date: latest -> oldest

```shell
todo ls
```

## List by given date

User need to provide date range:

- Start date: --start/-s
- End date: --end/-e

Then those tasks, whose done_date or created_date is in this range, will be displayed in a table.

```shell
todo ls -s 20241101 -e 20241130
```

Or list last week/month/year's tasks

```
todo ls --week
todo ls --month
todo ls --year
```


## List by given ids

User need to provide a task id/tasks' id

```shell
todo ls 1 2 3 4 ....
```

## List by given status

Status:

- todo: `--todo` search all tasks, whose status is todo or expr
- expr: `--expr` search all expr tasks
- done: `--done` search all done tasks


```
todo ls --todo
```
