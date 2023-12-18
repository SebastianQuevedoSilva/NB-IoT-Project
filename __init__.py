from flask import Flask
from flask_socketio import socketIO

app = Flask(__name__)

socketIO = SocketIO(app)