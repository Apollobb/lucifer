# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from salts.models import SaltCmdrun

class SaltCmdrunFilter(filters.FilterSet):
    class Meta:
        model = SaltCmdrun
        fields = {
            'user__username': ['exact', 'contains'],
            'cmd': ['contains'],
        }
