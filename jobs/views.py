# -*- coding: utf-8 -*-
# author: itimor

from jobs.serializers import JobsSerializer, JobGroupSerializer
from rest_framework import viewsets

from jobs.filters import JobsFilter
from jobs.models import Jobs, JobGroup


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    filter_class = JobsFilter


class JobGroupViewSet(viewsets.ModelViewSet):
    queryset = JobGroup.objects.all()
    serializer_class = JobGroupSerializer
