# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from hosts.models import Host, HostGroup

class HostFilter(filters.FilterSet):
    class Meta:
        model = Host
        fields = {
            'hostname': ['exact', 'contains'],
            'ip': ['exact', 'contains'],
            'group__name': ['exact'],
            'asset_type': ['exact'],
            'status': ['exact'],
            'os': ['exact', 'contains'],
            'cpu_num': ['exact'],
            'memory': ['exact'],
            'disk': ['exact'],
        }
