# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from hosts.models import Host, HostGroup, SaltServer, Upload
from users.models import User


class HostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(many=True, queryset=HostGroup.objects.all(), slug_field='name')
    class Meta:
        model = Host
        fields = ['url', 'hostname', 'ip', 'other_ip', 'group', 'asset_type', 'status', 'os', 'cpu_model', 'cpu_num',
                  'memory', 'disk', 'memo']


class HostGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostGroup
        fields = ['url', 'name', 'desc']


class SaltServerSerializer(serializers.ModelSerializer):
    ip = serializers.SlugRelatedField(queryset=Host.objects.all(), slug_field='hostname')

    class Meta:
        model = SaltServer
        fields = ['url', 'ip', 'port', 'apiurl', 'username', 'password']
        read_only_fields = ('apiurl',)


class UploadSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Upload
        fields = ['url', 'username', 'file', 'date']
