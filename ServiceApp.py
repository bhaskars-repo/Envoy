#
# Name:   Simple Flask Service
# Author: Bhaskar S
# Blog:   https://www.polarsparc.com
#

import socket
import sys
from datetime import datetime
from flask import Flask

app = Flask(__name__)
PORT = 0


@app.route('/first')
def first():
    return "{'Message': 'Hello from %s:%d', 'Timestamp': '%s'}" % (socket.gethostname(), PORT, datetime.now())


if __name__ == '__main__':
    if len(sys.argv) == 2:
        PORT = int(sys.argv[1])
        app.run(host='0.0.0.0', port=PORT)
