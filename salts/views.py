# -*- coding: utf-8 -*-
# author: itimor

import sys
import subprocess
from utils.timeout import timeout

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from salts.models import SaltServer, SaltCmdrun
from salts.serializers import SaltServerSerializer, SaltCmdrunSerializer
from salts.filters import SaltCmdrunFilter

@timeout(4)
def run(cmd):
    try:
        stdout = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #stdout = output.stdout.readlines()
        stderr = ''
    except:
        stdout = ''
        stderr = str(sys.exc_info())
    if len(stderr):
        return stderr
    else:
        return stdout


class SaltServerViewSet(viewsets.ModelViewSet):
    queryset = SaltServer.objects.all()
    serializer_class = SaltServerSerializer


class SaltCmdrunViewSet(viewsets.ModelViewSet):
    queryset = SaltCmdrun.objects.all()
    serializer_class = SaltCmdrunSerializer
    filter_class = SaltCmdrunFilter


@ api_view(['POST'])
def cmdrun(request):
    serializer = SaltCmdrunSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        cmd = request.data['cmd']
        results = run(cmd).stdout.readlines()
        return Response(results, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)