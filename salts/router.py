# -*- coding: utf-8 -*-
# author: itimor

from channels.routing import route, route_class
from .consumers import CmdrunConsumer

cmdrun_routing = [
    route_class(CmdrunConsumer),
]