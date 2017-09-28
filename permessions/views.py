# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets

from permessions.models import MethodChoices, Permessions
from permessions.serializers import MethodChoicesSerializer, PermessionsSerializer
from permessions.filters import PermessionsFilter


class MethodChoicesViewSet(viewsets.ModelViewSet):
    queryset = MethodChoices.objects.all()
    serializer_class = MethodChoicesSerializer


class PermessionsViewSet(viewsets.ModelViewSet):
    queryset = Permessions.objects.all()
    serializer_class = PermessionsSerializer
    filter_class = PermessionsFilter
