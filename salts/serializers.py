# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from salts.models import SaltServer, SaltCmdrun
from hosts.models import Host


class SaltServerSerializer(serializers.ModelSerializer):
    ip = serializers.SlugRelatedField(queryset=Host.objects.all(), slug_field='hostname')

    class Meta:
        model = SaltServer
        fields = ['url', 'id', 'ip', 'port', 'apiurl', 'username', 'password']
        read_only_fields = ('apiurl',)

class SaltCmdrunSerializer(serializers.ModelSerializer):
    ips = serializers.SlugRelatedField(many=True, queryset=Host.objects.all(), slug_field='hostname')
    class Meta:
        model = SaltCmdrun
        fields = ['id', 'ips', 'cmd', 'result']
        read_only_fields = ('result',)