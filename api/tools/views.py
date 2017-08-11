# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from tools.models import Duty
from serializers import DutySerializer
from filters import DutyFilter


class DutyViewSet(viewsets.ModelViewSet):
    queryset = Duty.objects.all()
    serializer_class = DutySerializer
    filter_class = DutyFilter
