"""Set config for todo-cmd"""

import rich_click as click

import todo_cmd.templates as t
from todo_cmd.language import TRANS
from todo_cmd.interface.config import CONFIG, set_config


@click.command()
@click.option("-l", "--list", is_flag=True, default=False, help=TRANS("config_list"))
@click.option("-e", "--edit", is_flag=True, default=False, help=TRANS("config_edit"))
def config(list: bool, edit: bool):
    if list:
        t.console.print(CONFIG)
    elif edit:
        t.info(TRANS("config_edit"))

        new_lang = t.ask(TRANS("config_ask_lang"), choices=["en", "zh"], default=CONFIG["language"])
        set_config("language", new_lang)

        new_ddl_delta = t.ask(TRANS("config_ask_ddl_delta"), default=CONFIG["ddl_delta"])
        set_config("ddl_delta", new_ddl_delta)

        t.done(TRANS("config_edit_done"))
    else:
        ctx = click.get_current_context()
        ctx.get_help()
