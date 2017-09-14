# -*- coding: utf-8 -*-
# author: itimor

import sys
import shlex
import subprocess
import json

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from salts.models import SaltServer, SaltCmdrun
from salts.serializers import SaltServerSerializer, SaltCmdrunSerializer


def execute(cmd):
    '''
    execute cmd
    '''
    commands = shlex.split(cmd)
    try:
        stdout = subprocess.check_output(commands)
        stderr = ''
    except:
        stdout = ''
        stderr = str(sys.exc_info()[1])

    if len(stderr):
        return stderr
    else:
        return stdout


class SaltServerViewSet(viewsets.ModelViewSet):
    queryset = SaltServer.objects.all()
    serializer_class = SaltServerSerializer


@api_view(['GET', 'POST'])
def cmdrun_list(request):
    if request.method == 'GET':
        cmdrun = SaltCmdrun.objects.all()
        serializer = SaltCmdrunSerializer(cmdrun, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        cmd = request.data['cmd']
        print(request.data)
        results = execute(cmd)
        print results.split('\n')
        cur_results = results.split('\n')
        print cur_results
        serializer = SaltCmdrunSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(cur_results, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)