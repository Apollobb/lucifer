# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets

from hosts.filters import HostFilter
from hosts.models import Host, HostGroup
from hosts.serializers import HostSerializer, HostGroupSerializer
from hosts.permissions import UserPerms


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_class = HostFilter


class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = HostGroup.objects.all()
    serializer_class = HostGroupSerializer
    permission_classes = (UserPerms,)