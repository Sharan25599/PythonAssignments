import datetime

def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.datetime.strptime(t1, format)
    dt2 = datetime.datetime.strptime(t2, format)
    delta = dt1 - dt2

    return str(abs(int(delta.total_seconds())))