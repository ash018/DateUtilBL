from flask import Flask, jsonify
from datetime import datetime
import socket
docker_short_id = socket.gethostname()

app = Flask(__name__)


def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    return str(int(abs((t1-t2).total_seconds())))


def run_taskAFromB():
    arr = list()
    f = open("input.txt", "r")
    count = 0
    x = 0
    arr = list()
    while True:
        count += 1
        line = f.readline()
        if(count == 1):
            x = int(line)
        else:
            if line.strip() != '':
                arr.append(line.strip())

        if not line:
            break

    f.close()
    sz = len(arr)
    deltaList = list()
    if(sz > 0 and sz % 2 == 0):
        for j in range(0, len(arr), 2):
            delta = time_delta(arr[j], arr[j+1])
            deltaList.append(delta)
    return deltaList


@app.route('/')
def hello_world():
    deltaList = run_taskAFromB()
    if len(deltaList) == 0:
        return jsonify(message="Error in Format", id=docker_short_id, value=deltaList)
    else:
        return jsonify(message="Success", id=docker_short_id, value=deltaList)


if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
