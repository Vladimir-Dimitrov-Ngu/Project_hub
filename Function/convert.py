import pandas as pd
def convert_timestamp(data,column, format_: str='%Y-%m-%d %H:%M:%S'):
    timestamp = data[column]
    timestamp = timestamp.str.replace('.000', '')
    timestamp = pd.to_datetime(timestamp, format=format_)
    return timestamp
