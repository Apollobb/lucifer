# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from permessions.models import Permessions

class PermessionsFilter(filters.FilterSet):
    class Meta:
        model = Permessions
        fields = {
            'id': ['exact'],
            'name': ['exact'],
            'code': ['exact'],
        }