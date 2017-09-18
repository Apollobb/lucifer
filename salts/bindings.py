# -*- coding: utf-8 -*-
# author: itimor

from channels_api.bindings import ResourceBinding

from salts.models import SaltCmdrun
from salts.serializers import SaltCmdrunSerializer

class SaltCmdrunBinding(ResourceBinding):

    model = SaltCmdrun
    stream = "cmdrun"
    serializer_class = SaltCmdrunSerializer
    queryset = SaltCmdrun.objects.all()