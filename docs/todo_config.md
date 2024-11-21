# Command about configuration

## List all configuration

```shell
todo config

---
{'language': 'en', 'ddl_delta': 43200}
```

## Modify configuration

```
todo config ${attr} ${value}

# e.g. set language to Chinese
todo config language zh
```

## Configuration

### `language`

- zh: Chinese
- en: English

### `ddl_delta`

When adding a todo with out specify its deadline,
`todo-cmd` will add a default time delta: `ddl_delta`.

`ddl_delta` must be a integer larger than 0, metric is second.

`ddl_delta`'s default value is 1 day.
