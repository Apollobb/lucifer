# -*- coding: utf-8 -*-
# author: itimor

from salts.cmdrun import run
import json
import os

salt_log = '/tmp/salt/'
os.popen(f'mkdir -p {salt_log}')


def cmdrun_receive(message):
    text = message.content['text']
    request = json.loads(text)
    cmd = request['cmd']

    results = run(cmd).stdout
    for result in results:
        message.reply_channel.send({'text':result.decode('utf-8')}, True)


def cmdlog_receive(message):
    text = message.content['text']
    request = json.loads(text)
    cmd = request['cmd']

    results = run(cmd).stdout
    for result in results:
        message.reply_channel.send({'text':result.decode('utf-8')}, True)

def viewfile_receive(message):
    text = message.content['text']
    request = json.loads(text)
    filename = request['filename']

    cmd = f'cat {filename}'
    results = run(cmd).stdout
    for result in results:
        message.reply_channel.send({'text':result.decode('utf-8')}, True)