from datetime import datetime
from typing import Optional

import todo_cmd.templates as t
from todo_cmd.language import TRANS


def val_date_fmt(date_str: str) -> Optional[datetime]:
    """validate the format of given datetime string,
    if it is valid, convert it to `datetime.datetime` object,
    otherwise, retrun None

    Support
    - "%Y-%m-%d_%H:%M:%S"
    - "%Y-%m-%d",
    - "%Y%m%d"

    Args:
        date_str (str): datetime string

    Returns:
        Optional[datetime]: if valid return dt, otherwise None
    """
    if type(date_str) != str:
        return None
    
    formats = [
        "%Y-%m-%d_%H:%M:%S",  # 格式 1: "2024-01-01_12:30:45"
        "%Y-%m-%d",           # 格式 2: "2024-01-01"
        "%Y%m%d"              # 格式 3: "20240101"
    ]
    
    for fmt in formats:
        try:
            # 尝试解析日期字符串
            dt = datetime.strptime(date_str, fmt)
            return dt  # 如果成功解析，返回 True
        except ValueError:
            continue  # 如果解析失败，尝试下一个格式
    
    return None


def val_date_fmt_callback(ctx, param, value):
    """validation for --deadline or other date option"""
    if value is None:
        return None
    try:
        dt = val_date_fmt(value)
    except:
        t.error(f"{TRANS('input_date')}: {value}")
        t.error(TRANS("date_fmt_not_support"))
        exit(1)

    if not dt:
        t.error(f"{TRANS('input_date')}: {value}")
        t.error(TRANS("date_fmt_not_support"))
        exit(1)

    return dt
