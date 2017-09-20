# -*- coding: utf-8 -*-
# author: itimor

from salts.cmdrun import run
import json
import time
from channels.generic.websockets import WebsocketConsumer

class CmdrunConsumer(WebsocketConsumer):
    http_user = True
    strict_ordering = False

    def connection_groups(self, **kwargs):
        return ["test"]

    def connect(self, message, **kwargs):
        self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        request = json.loads(text)
        hosts = request['hosts']
        user = request['user']
        cmd = request['cmd']

        results = run(cmd).stdout
        for result in results:
            if result:  # 把内容发送到前端
                self.send(text=result.decode('utf-8'), bytes=bytes)

    def disconnect(self, message, **kwargs):
        pass