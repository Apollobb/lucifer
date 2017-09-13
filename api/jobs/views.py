# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from jobs.models import Jobs, JobGroup
from api.jobs.serializers import JobsSerializer, JobGroupSerializer
from api.jobs.filters import JobsFilter


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    filter_class = JobsFilter


class JobGroupViewSet(viewsets.ModelViewSet):
    queryset = JobGroup.objects.all()
    serializer_class = JobGroupSerializer
