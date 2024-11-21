"""Set config for todo-cmd"""

import rich_click as click

import todo_cmd.templates as t
from todo_cmd.language import TRANS
from todo_cmd.interface.config import CONFIG, set_config


@click.command()
@click.argument("attr", type=str, default="")
@click.argument("value", type=str, default="")
def config(attr: str, value: str):
    if attr == "":
        t.console.print(CONFIG)
        return 0
    if attr != "" and value == "":
        t.error(TRANS("empty_attr_value"))
        return 0
    set_config(attr, value)