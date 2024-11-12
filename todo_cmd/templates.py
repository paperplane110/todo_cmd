"""Some prints templates
support colors: https://rich.readthedocs.io/en/stable/appendix/colors.html
"""
from functools import wraps

from rich.console import Console
from rich.prompt import Prompt

console = Console()

DONE_MARK = "[default on green4] √ [/]"
TODO_MARK = "[default on dodger_blue2] - [/]"
ERROR_MARK = "[default on red] x [/]"
ASK_MARK = "[default on deep_sky_blue1] ? [/]"
INFO_MARK = "[default on bright_black] * [/]"


@wraps(console.print)
def done(*args, **kwargs):
    console.print(DONE_MARK, *args, **kwargs)


@wraps(console.print)
def todo(*args, **kwargs):
    console.print(TODO_MARK, *args, **kwargs)


@wraps(console.print)
def error(*args, **kwargs):
    console.print(ERROR_MARK, *args, **kwargs)


@wraps(Prompt.ask)
def ask(prompt: str, **kwargs):
    res = Prompt.ask(f"{ASK_MARK} {prompt}", **kwargs)
    return res


@wraps(console.print)
def info(*args, **kwargs):
    console.print(INFO_MARK, *args, **kwargs)
