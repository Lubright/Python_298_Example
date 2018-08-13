import time


def GetTime(TimeFormat):
    now = time.time()
    local_time = time.localtime(now)
    result = time.strftime(TimeFormat)
    return result


if __name__ == '__main__':
    print(GetTime('%Y-%m-%d %H:%M:%S'))
