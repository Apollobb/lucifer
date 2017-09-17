# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from salts.models import SaltServer, SaltCmdrun
from hosts.models import Host
from users.models import User

class SaltServerSerializer(serializers.ModelSerializer):
    ip = serializers.SlugRelatedField(queryset=Host.objects.all(), slug_field='hostname')
    class Meta:
        model = SaltServer
        fields = ['url', 'id', 'ip', 'port', 'apiurl', 'username', 'password']
        read_only_fields = ('apiurl',)

class SaltCmdrunSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    hosts = serializers.SlugRelatedField(many=True, queryset=Host.objects.all(), slug_field='hostname')
    class Meta:
        model = SaltCmdrun
        fields = ['url', 'id', 'user', 'hosts', 'cmd']

    def create(self, validated_data):
        print(validated_data)
        instance = SaltCmdrun.objects.create(**validated_data)
        print(instance)
        return instance