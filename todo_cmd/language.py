import os
import json
from typing import Literal

from rich.console import Console

import todo_cmd.templates as t
from todo_cmd.interface.config import CONFIG

console = Console()
current_dir = os.path.dirname(os.path.abspath(__file__))
language_setting_path = os.path.join(current_dir, "language.json")

with open(language_setting_path, "r", encoding="utf-8") as fp:
    lang_dict = json.load(fp)

LANG = Literal["zh", "en"]

def i2n(lang: LANG):
    def trans(key: str) -> str:
        try:
            return lang_dict[key][lang]
        except KeyError:
            console.print(t.error(f"Cannot find  {lang}:{key} in language.json"))
            exit(1)
    return trans


if CONFIG:
    TRANS = i2n(CONFIG["language"])
else:
    TRANS = None
