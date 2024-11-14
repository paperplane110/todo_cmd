# List todo

## List all tasks

Sorted by:

- status: expr, todo, done
- created_date: latest -> oldest

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

or use `--verbose/-v` to show more info

```shell
todo ls -v
```

```
┏━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ id ┃ Status ┃ Task                                 ┃      Deadline       ┃    Created Date     ┃     Finish Date     ┃
┡━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ 10 │  expr  │ Apply a card for my electric-bike    │ 2024-11-10_00:00:00 │ 2024-11-12_22:39:12 │                     │
├────┼────────┼──────────────────────────────────────┼─────────────────────┼─────────────────────┼─────────────────────┤
│ 9  │  todo  │ ask Liuke about perf monitor scripts │ 2024-11-13_10:32:22 │ 2024-11-12_22:32:25 │                     │
├────┼────────┼──────────────────────────────────────┼─────────────────────┼─────────────────────┼─────────────────────┤
│ 8  │  done  │ start a pr in rich                   │ 2024-11-12_01:25:43 │ 2024-11-12_01:25:43 │ 2024-11-12_01:25:43 │
│ 7  │  done  │ refactor template and ask            │ 2024-11-12_11:26:57 │ 2024-11-11_23:27:00 │ 2024-11-11_23:54:39 │
│ 6  │  done  │ find ICBC card                       │ 2024-11-12_10:48:00 │ 2024-11-11_22:48:03 │ 2024-11-12_01:31:18 │
│ 4  │  done  │ finish todo rm                       │ 2024-11-10_23:24:05 │ 2024-11-10_23:24:05 │ 2024-11-10_23:24:05 │
│ 3  │  done  │ go to ICBC update ID info            │ 2024-11-12_00:00:00 │ 2024-11-10_22:39:23 │ 2024-11-12_22:31:43 │
│ 1  │  done  │ add some translation                 │ 2024-11-10_22:20:58 │ 2024-11-10_22:20:58 │ 2024-11-10_22:20:58 │
└────┴────────┴──────────────────────────────────────┴─────────────────────┴─────────────────────┴─────────────────────┘
```

## List by given ARGUMENTS


```
todo ls ARGUMENTS
```

- `ARGUMENTS` can be task id/tasks' id

```shell
todo ls 1

# or
todo ls 1 2 3 4
```

Or if you want to know what you have done in the last week/month/year

- `today/t`: today
- `yest/y`: yesterday
- `week/w`: last week
- `month/m`: last month
- `year`: last year

```
todo ls y
todo ls w
todo ls m
```

Or, you would like to know the next day/weeks/month's plan:

- `tmr`: tomorrow
- `nw`: next week
- `nm`: next month
- `ny`: next year

## List by given date

User need to provide date range:

- Start date: --start/-s
- End date: --end/-e

Then those tasks, whose done_date or created_date is in this range, will be displayed in a table.

```shell
todo ls -s 20241101 -e 20241130
```


## List by given status

Status:

- todo: `--todo` search all tasks, whose status is todo or expr
- expr: `--expr` search all expr tasks
- done: `--done` search all done tasks


```
todo ls --todo
```

## Options Composition

- 🕶 When `id or ids` is given, other options will be omitted

```shell
# will only display task 1 2 3
todo ls 1 2 3 --done
```

- `yest/week/month/year/tmr/nw/nm/ny` can work with status option

```shell
# search what should be done in the next week
todo ls nw --todo

# search what has been done on yesterday
todo ls yest --done
```

- ✅ Valid

```shell
# Search tasks in last week, whose status is done
todo ls week --done

# Search tasks between 20240101 and 20241231, whose status is done
todo ls -s 20240101 -e 20241231 --done
```

- ❌ Invalid

```shell
todo ls week -s 20240101 -e 20241231
todo ls --todo --expr
```