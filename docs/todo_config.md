# Command about configuration

## List all configuration

```shell
todo config --list

---
{'language': 'en', 'ddl_delta': 3}
```

## Modify configuration

```
todo config --edit
```

## Configuration

### `language`

- zh: Chinese
- en: English

### `ddl_delta`

When adding a todo without specify its deadline,
`todo-cmd` will add a default time delta: `ddl_delta`.

`ddl_delta` must be an integer larger than 0, metric is day.

`ddl_delta`'s default value is 3 day.
