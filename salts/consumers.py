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

        result = run(cmd).stdout.readline()  # 获取内容

        while True:
            if result:  # 把内容发送到前端
                print(result)
                self.send(text=result.decode('utf-8'), bytes=bytes)
            time.sleep(1)

    def disconnect(self, message, **kwargs):
        pass