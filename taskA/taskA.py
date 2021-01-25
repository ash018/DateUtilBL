from datetime import datetime

def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    return str(int(abs((t1-t2).total_seconds())))


def run_taskA():
    itr = int(input())

    for i in range(itr):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)

run_taskA()

