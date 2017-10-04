# -*- coding: utf-8 -*-
# author: itimor

from hosts.filters import HostFilter
from rest_framework import viewsets

from hosts.models import Host, HostGroup
from hosts.serializers import HostSerializer, HostGroupSerializer
from permessions import perms


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_class = HostFilter
    permission_classes = (perms.UserPerms,)


class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = HostGroup.objects.all()
    serializer_class = HostGroupSerializer