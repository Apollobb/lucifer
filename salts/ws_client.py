# -*- coding: utf-8 -*-
# author: itimor

import websocket
import json

import websocket
import _thread
import time

from websocket import create_connection

ws = create_connection("ws://api.lucifer.com/" + '8000'')
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result = ws.recv()
print("Received '%s'" % result)
ws.close()
