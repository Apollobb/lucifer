# -*- coding: utf-8 -*-
# author: itimor

from channels.routing import route
from salts.consumers import cmdrun_receive, viewfile_receive

salt_routing = [
    route('websocket.receive',cmdrun_receive, path='/cmdrun/'),
    route('websocket.receive',viewfile_receive, path='/viewfile/'),
]