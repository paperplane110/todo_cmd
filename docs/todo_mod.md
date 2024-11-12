# Modify a task

## 可以修改的属性

- 任务内容：task
- 任务状态：status
- 截止日期：ddl
- （待定）标签：tags

## 仅提供 `id`

```shell
todo mod ${id}

todo m ${id}
```

仅提供 `id` 时，会逐条询问需要修改的点

## 提供修改属性

当具体指定要修改的属性时，只修改指定的属性，不对其他属性进行提问。

属性作为 options，有：

- `--task`/`-t`
- `--status`/`-s`
- `--ddl`/`-ddl`

使用方法为:

```shell
todo mod 4 --status done

# or
todo mod 4 -s done

# or
todo mod 4 --status done --task "complete feat1"
```

注意 `--task` 后的参数用引号括起来
