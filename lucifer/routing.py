# -*- coding: utf-8 -*-
# author: itimor

from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from salts.bindings import SaltCmdrunBinding

class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
      'questions': SaltCmdrunBinding.consumer
    }

channel_routing = [
    route_class(APIDemultiplexer)
]