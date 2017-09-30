# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets

from permessions.models import MethodChoices, ApiPermessions
from permessions.serializers import MethodChoicesSerializer, ApiPermessionsSerializer
from permessions.filters import ApiPermessionsFilter


class MethodChoicesViewSet(viewsets.ModelViewSet):
    queryset = MethodChoices.objects.all()
    serializer_class = MethodChoicesSerializer


class ApiPermessionsViewSet(viewsets.ModelViewSet):
    queryset = ApiPermessions.objects.all()
    serializer_class = ApiPermessionsSerializer
    filter_class = ApiPermessionsFilter

