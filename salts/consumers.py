# -*- coding: utf-8 -*-
# author: itimor

from salts.cmdrun import run
import json
import time
import os
from channels.generic.websockets import WebsocketConsumer

class CmdrunConsumer(WebsocketConsumer):
    http_user = True

    def connection_groups(self, **kwargs):
        return ["cmdrun"]

    def connect(self, message, **kwargs):
        self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        request = json.loads(text)
        hosts = request['hosts']
        user = request['user']
        cmd = request['cmd']
        print(request)

        results = run(cmd).stdout
        for result in results:
            if result:  # 把内容发送到前端
                self.send(text=result.decode('utf-8'), bytes=bytes)

    def disconnect(self, message, **kwargs):
        pass


class SaltInstallConsumer(WebsocketConsumer):
    http_user = True

    def connection_groups(self, **kwargs):
        return ["state_install"]

    def connect(self, message, **kwargs):
        self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        request = json.loads(text)
        hosts = request['hosts']
        user = request['user']
        sls = request['sls']
        log_file = request['log_file']

        salt_log = '/tmp/salt/' + log_file

        with open(salt_log, 'w+') as fn:
            fn.write('{} {}\n'.format(time.time(),user))
            fn.write('{} {}\n'.format(time.time(),hosts))
            fn.write('{} {}\n'.format(time.time(),sls))
            fn.write('{} {}\n'.format(time.time(),log_file))


        results = run('tail -f {}'.format(salt_log)).stdout
        print(results)
        for result in results:
            if result:  # 把内容发送到前端
                self.send(text=result.decode('utf-8'), bytes=bytes)

    def disconnect(self, message, **kwargs):
        pass