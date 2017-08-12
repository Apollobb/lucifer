# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from tools.models import Duty, Upload
from serializers import DutySerializer, UploadSerializer
from filters import DutyFilter


class DutyViewSet(viewsets.ModelViewSet):
    queryset = Duty.objects.all()
    serializer_class = DutySerializer
    filter_class = DutyFilter


class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
