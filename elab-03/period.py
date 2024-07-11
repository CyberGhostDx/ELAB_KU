def read_hour():
    return int(input("Enter hour: "))


def read_minute():
    return int(input("Enter minute: "))


def read_second():
    return int(input("Enter second: "))


def to_seconds(hours, minute, second):
    return hours * 3600 + minute * 60 + second


def time_elapsed(start, finish):
    dt = finish - start
    dh = dt // 3600
    dm = dt // 60 % 60
    ds = dt % 60
    return f"{dh} hours {dm} minutes {ds} seconds."
