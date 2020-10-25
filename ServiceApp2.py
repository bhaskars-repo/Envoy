#
# Name:   Simple Flask Service 2
# Author: Bhaskar S
# Blog:   https://www.polarsparc.com
#

import socket
import sys
from datetime import datetime
from flask import Flask
import random

app = Flask(__name__)
PORT = 0


@app.route('/second')
def first():
    return "{'Message': 'Greetings from %s:%d', 'Token': '%d', 'Timestamp': '%s'}" %\
           (socket.gethostname(), PORT, random.randint(1, 100), datetime.now())


if __name__ == '__main__':
    if len(sys.argv) == 2:
        PORT = int(sys.argv[1])
        app.run(host='0.0.0.0', port=PORT)
