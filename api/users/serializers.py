# -*- coding: utf-8 -*-
# author: itimor

from users.models import User, Group, Role
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name')
    roles = serializers.SlugRelatedField(queryset=Role.objects.all(), slug_field='name')
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'name', 'avatar', 'group', 'is_active', 'roles', 'avatar', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'],
                    email=validated_data['email'],
                    name=validated_data['name'],
                    group=validated_data['group'],
                    roles=validated_data['roles'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url','id', 'name', 'desc')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('url', 'id', 'name', 'cnname', 'desc')