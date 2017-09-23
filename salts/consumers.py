# -*- coding: utf-8 -*-
# author: itimor

from salts.cmdrun import run
import json
from datetime import datetime
import os
from channels.generic.websockets import WebsocketConsumer


salt_log = '/tmp/salt/'
os.popen(f'mkdir -p {salt_log}')


class CmdrunConsumer(WebsocketConsumer):
    def receive(self, text=None, bytes=None, **kwargs):
        request = json.loads(text)
        hosts = request['hosts']
        user = request['user']
        cmd = request['cmd']

        results = run(cmd)
        for result in results:
            self.send(text=result.decode('utf-8'))


class SaltInstallConsumer(WebsocketConsumer):
    def receive(self, text=None, bytes=None, **kwargs):
        request = json.loads(text)
        hosts = request['hosts']
        user = request['user']
        sls = request['sls']
        log_file = request['log_file']

        soft_log = '{}{}'.format(salt_log, log_file)
        with open(soft_log, 'w+') as fn:
            fn.write(f'{datetime.now()} {user}\n')
            fn.write(f'{datetime.now()} {hosts}\n')
            fn.write(f'{datetime.now()} {sls}\n')
            fn.write(f'{datetime.now()} {log_file}\n')

        results = run(f'cat {soft_log}').stdout
        for result in results:
            if result:  # 把内容发送到前端
                self.send(text=result.decode('utf-8'), bytes=bytes)

class ViewFileConsumer(WebsocketConsumer):
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
                fn.write(f'{datetime.now()} {user}\n')
                fn.write(f'{datetime.now()} {hosts}\n')