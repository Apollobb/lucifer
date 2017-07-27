# -*- coding: utf-8 -*-
# author: itimor

from users.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.SlugRelatedField(many=True, queryset=Group.objects.all(), slug_field='name')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'name', 'group', 'is_admin', 'roles')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'slug', 'name')
