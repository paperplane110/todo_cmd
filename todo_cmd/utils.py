from datetime import datetime
from typing import Optional

def validate_date_format(date_str) -> Optional[datetime]:
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