# -*- coding: utf-8 -*-
# author: itimor

def ws_message(message):
    message.reply_channel.send({
        "text": message.content['text'],
    })