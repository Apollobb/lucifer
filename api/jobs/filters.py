# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from jobs.models import Jobs

class JobsFilter(filters.FilterSet):
    class Meta:
        model = Jobs
        fields = {
            'name': ['exact', 'contains'],
            'deploy_status': ['exact'],
            'group__name': ['exact']
        }
