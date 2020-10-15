from datetime import datetime, timedelta

def convert_timestamp(time_str):
    if not time_str:
        return None
    time_str = time_str.split("T")[0]
    return datetime.strptime(time_str, "%Y-%m-%d").date()
