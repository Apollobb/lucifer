# -*- coding: utf-8 -*-
# author: itimor

from channels.routing import route, include
from salts.router import cmdrun_routing

channel_routing = [
    include(cmdrun_routing, path='^/cmdrun'),
]