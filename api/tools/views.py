# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from tools.models import Duty, Upload
from api.tools.serializers import DutySerializer, UploadSerializer
from api.tools.filters import DutyFilter, UploadFilter


class DutyViewSet(viewsets.ModelViewSet):
    queryset = Duty.objects.all()
    serializer_class = DutySerializer
    filter_class = DutyFilter


class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    filter_class = UploadFilter
