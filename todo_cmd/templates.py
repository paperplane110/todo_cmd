"""Some prints templates
support colors: https://rich.readthedocs.io/en/stable/appendix/colors.html
"""

def done(content: str):
    return f"[default on green4] √ [/] {content}"


def todo(content: str):
    return f"[default on dodger_blue2] - [/] {content}"


def error(content: str):
    return f"[default on red] x [/] {content}"


def question(content: str):
    return f"[default on deep_sky_blue1] ? [/] {content}"


def info(content: str):
    return f"[default on bright_black] * [/] {content}"

