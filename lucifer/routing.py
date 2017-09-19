# -*- coding: utf-8 -*-
# author: itimor

from channels.routing import route_class
from salts.consumers import CmdrunDemultiplexer

channel_routing = [
    route_class(CmdrunDemultiplexer)
]