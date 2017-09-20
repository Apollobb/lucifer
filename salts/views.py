# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets

from salts.models import SaltServer, SaltCmdrun, SaltState
from salts.serializers import SaltServerSerializer, SaltCmdrunSerializer, SaltStateSerializer
from salts.filters import SaltCmdrunFilter



class SaltServerViewSet(viewsets.ModelViewSet):
    queryset = SaltServer.objects.all()
    serializer_class = SaltServerSerializer


class SaltCmdrunViewSet(viewsets.ModelViewSet):
    queryset = SaltCmdrun.objects.all()
    serializer_class = SaltCmdrunSerializer
    filter_class = SaltCmdrunFilter


class SaltStateViewSet(viewsets.ModelViewSet):
    queryset = SaltState.objects.all()
    serializer_class = SaltStateSerializer