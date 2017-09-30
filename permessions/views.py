# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets

from permessions.models import ApiPermessions
from permessions.serializers import ApiPermessionsSerializer
from permessions.filters import ApiPermessionsFilter


class ApiPermessionsViewSet(viewsets.ModelViewSet):
    queryset = ApiPermessions.objects.all()
    serializer_class = ApiPermessionsSerializer
    filter_class = ApiPermessionsFilter

