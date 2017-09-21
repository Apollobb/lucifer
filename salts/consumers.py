# -*- coding: utf-8 -*-
# author: itimor

from salts.cmdrun import run
import json
import time
import os
from channels.generic.websockets import WebsocketConsumer

salt_log = '/tmp/salt/'
os.popen('mkdir -p %s' % salt_log)

class CmdrunConsumer(WebsocketConsumer):
    http_user = True

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


class SaltInstallConsumer(WebsocketConsumer):
    http_user = True

    def connect(self, message, **kwargs):
        self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        request = json.loads(text)
        hosts = request['hosts']
        user = request['user']
        sls = request['sls']
        log_file = request['log_file']

        soft_log = salt_log + log_file
        with open(soft_log, 'w+') as fn:
            fn.write('{} {}\n'.format(time.time(),user))
            fn.write('{} {}\n'.format(time.time(),hosts))
            fn.write('{} {}\n'.format(time.time(),sls))
            fn.write('{} {}\n'.format(time.time(),log_file))


        results = run('cat {}'.format(salt_log)).stdout
        for result in results:
            if result:  # 把内容发送到前端
                self.send(text=result.decode('utf-8'), bytes=bytes)