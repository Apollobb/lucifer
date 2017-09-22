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
    def connect(self, message, **kwargs):
        self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        request = json.loads(text)
        hosts = request['hosts']
        user = request['user']
        sls = request['sls']
        log_file = request['log_file']

        soft_log = '{}{}'.format(salt_log, log_file)
        with open(soft_log, 'w+') as fn:
            fn.write('{} {}\n'.format(time.time(),user))
            fn.write('{} {}\n'.format(time.time(),hosts))
            fn.write('{} {}\n'.format(time.time(),sls))
            fn.write('{} {}\n'.format(time.time(),log_file))

        results = run('cat {}'.format(soft_log)).stdout
        for result in results:
            if result:  # 把内容发送到前端
                self.send(text=result.decode('utf-8'), bytes=bytes)

class ViewFileConsumer(WebsocketConsumer):
    def connect(self, message, **kwargs):
        self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        request = json.loads(text)
        action = request['action']
        hosts = request['data']['hosts']
        user = request['data']['user']
        filename = request['data']['filename']

        file_path = f'/etc/sysconfig/{filename}'
        results = run(f'cat {file_path}').stdout
        for result in results:
            if result:  # 把内容发送到前端
                self.send(text=result.decode('utf-8'), bytes=bytes)
        if action == 'edit':
            with open(file_path, 'w+') as fn:
                fn.write('{} {}\n'.format(time.time(),user))
                fn.write('{} {}\n'.format(time.time(),hosts))