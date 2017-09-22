# -*- coding: utf-8 -*-
# author: itimor

from channels.routing import route_class
from .consumers import CmdrunConsumer, SaltInstallConsumer, ViewFileConsumer

salt_routing = [
    route_class(CmdrunConsumer, path='/cmdrun/'),
    route_class(SaltInstallConsumer, path='/state_install/'),
    route_class(ViewFileConsumer, path='/viewfile/'),
]