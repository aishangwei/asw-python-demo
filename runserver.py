
from flask import Flask
import datetime
import socket

app = Flask(__name__)


@app.route('/')
def hello_world():
    date_now = datetime.datetime.now()
    hostname = socket.gethostname()

    return "主机名：" + str(hostname) + "当前的日期和时间是：" + str(date_now)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')


