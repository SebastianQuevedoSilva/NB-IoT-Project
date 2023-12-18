# Author: Sebastian Quevedo Silva
# Date: December 17, 2023
from flask import Flask
from flask_socketio import socketIO

app = Flask(__name__)

socketIO = SocketIO(app)
