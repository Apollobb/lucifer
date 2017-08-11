# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from tools.models import Duty

class DutyFilter(filters.FilterSet):
    class Meta:
        model = Duty
        fields = {
            'username': ['exact', 'contains'],
            'shift': ['exact'],
            'create_time': ['exact', 'contains'],
        }
