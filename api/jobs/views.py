# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from jobs.models import Jobs, JobGroup
from serializers import JobsSerializer, JobGroupSerializer

class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer


class JobGroupViewSet(viewsets.ModelViewSet):
    queryset = JobGroup.objects.all()
    serializer_class = JobGroupSerializer