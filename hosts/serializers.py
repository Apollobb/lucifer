# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from hosts.models import Host, HostGroup


class HostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(many=True, queryset=HostGroup.objects.all(), slug_field='name')
    class Meta:
        model = Host
        fields = ['url', 'id', 'hostname', 'ip', 'other_ip', 'group', 'asset_type', 'status', 'os', 'cpu_model', 'cpu_num',
                  'memory', 'disk', 'memo']


class HostGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostGroup
        fields = ['url', 'id', 'name', 'desc']