# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from hosts.models import Host, HostGroup, SaltServer
from serializers import HostSerializer, HostGroupSerializer, SaltServerSerializer
from filters import HostFilter


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_class = HostFilter


class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = HostGroup.objects.all()
    serializer_class = HostGroupSerializer


class SaltServerViewSet(viewsets.ModelViewSet):
    queryset = SaltServer.objects.all()
    serializer_class = SaltServerSerializer


