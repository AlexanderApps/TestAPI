from datetime import datetime

def datetime_to_timestamp(str_datetime):
    dt = datetime.strptime(str_datetime, "%Y-%m-%dT%H:%M:%S")
    return dt.timestamp()