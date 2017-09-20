# -*- coding: utf-8 -*-
# author: itimor

from channels.routing import route, include
from salts.router import salt_routing

channel_routing = [
    include(salt_routing, path='^/salt'),
]