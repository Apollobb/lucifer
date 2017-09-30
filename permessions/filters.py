# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from permessions.models import ApiPermessions

class ApiPermessionsFilter(filters.FilterSet):
    class Meta:
        model = ApiPermessions
        fields = {
            'id': ['exact'],
            'name': ['exact'],
            'code': ['exact'],
        }