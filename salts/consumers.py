# -*- coding: utf-8 -*-
# author: itimor

from channels.generic.websockets import WebsocketDemultiplexer
from salts.bindings import SaltCmdrunBinding

class CmdrunDemultiplexer(WebsocketDemultiplexer):

    consumers = {
      'cmdrun': SaltCmdrunBinding.consumer
    }
