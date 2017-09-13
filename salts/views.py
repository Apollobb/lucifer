# -*- coding: utf-8 -*-
# author: itimor

import sys
from subprocess import check_output

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
    result = {}
    try:
        stdout = check_output(cmd)
        stderr = ''
    except:
        stdout = ''
        stderr = str(sys.exc_info())
    result['stdout'] = stdout
    result['stderr'] = stderr
    return result


class SaltServerViewSet(viewsets.ModelViewSet):
    queryset = SaltServer.objects.all()
    serializer_class = SaltServerSerializer


@api_view(['GET', 'POST'])
def cmdrun_list(request):
    """
    展示所有存在的snippet, 或建立新的snippet
    """
    if request.method == 'GET':
        cmdrun = SaltCmdrun.objects.all()
        serializer = SaltCmdrunSerializer(cmdrun, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SaltCmdrunSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cmdrun_detail(request, pk):
    """
    展示, 更新或删除一个snippet
    """
    try:
        cmdrun = SaltCmdrun.objects.get(pk=pk)
    except SaltCmdrun.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SaltCmdrunSerializer(cmdrun)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SaltCmdrunSerializer(cmdrun, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cmdrun.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)