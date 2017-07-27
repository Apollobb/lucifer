# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from hosts.models import Host, HostGroup, SaltServer, Upload

class HostSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.SlugRelatedField(queryset=HostGroup.objects.all(), slug_field='name')
    class Meta:
        model = Host
        fields = ['url', 'hostname', 'ip', 'other_ip', 'group', 'asset_type', 'status', 'os', 'cpu_model', 'cpu_num',
                  'memory', 'disk', 'memo']


class HostGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HostGroup
        fields = ['url', 'name', 'desc']


class SaltServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SaltServer
        fields = ['url', 'ip', 'port', 'apiurl', 'username', 'password']


class UploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upload
        fields = ['url', 'username', 'headImg', 'date']