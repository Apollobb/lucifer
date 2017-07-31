# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from hosts.models import Host, HostGroup, SaltServer, Upload
from serializers import HostSerializer, HostGroupSerializer, SaltServerSerializer, UploadSerializer
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


class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
