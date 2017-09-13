# -*- coding: utf-8 -*-
# author: itimor

from hosts.filters import HostFilter
from rest_framework import viewsets

from hosts.models import Host, HostGroup
from hosts.serializers import HostSerializer, HostGroupSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_class = HostFilter


class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = HostGroup.objects.all()
    serializer_class = HostGroupSerializer