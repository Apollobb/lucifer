import logging

from channels import Group


GROUP_NAME = 'deploy'
logger = logging.getLogger(__name__)


def ws_connect(message):
    message.reply_channel.send({'accept': True})
    Group(GROUP_NAME).add(message.reply_channel)


def ws_disconnect(message):
    Group(GROUP_NAME).discard(message.reply_channel)


def ws_receive(message):
    data = {"aa":1, "cc":2}
    Group(GROUP_NAME).send({'text': json.dumps(data)})