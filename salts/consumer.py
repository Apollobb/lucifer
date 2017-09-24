import logging

from channels import Group
from channels.handler import AsgiHandler
from django.http import HttpResponse

from salts.cmdrun import run
import json
from datetime import datetime

logger = logging.getLogger(__name__)
GROUP_NAME = 'cmdrun'

def http_consumer(message):
    response = HttpResponse(message.content, content_type='text/plain')
    for chunk in AsgiHandler.encode_response(response):
        logger.debug(chunk)
        message.reply_channel.send(chunk)


def ws_connect(message):
    message.reply_channel.send({'accept': True})
    Group(GROUP_NAME).add(message.reply_channel)


def ws_disconnect(message):
    Group(GROUP_NAME).discard(message.reply_channel)


def ws_receive(message):
    text = message.content['text']
    request = json.loads(text)
    cmd = request['cmd']

    results = run(cmd)
    for result in results:
        Group(GROUP_NAME).send({'text':result.decode('utf-8')}, True)  #