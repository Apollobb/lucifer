# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from permessions.models import MethodChoices, ApiPermessions


class MethodChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodChoices
        fields = ['url', 'id', 'name', 'code']


class ApiPermessionsSerializer(serializers.ModelSerializer):
    choices = serializers.SlugRelatedField(many=True, queryset=MethodChoices.objects.all(), slug_field='code')
    class Meta:
        model = ApiPermessions
        fields = ['url', 'id', 'name', 'user', 'apiuri', 'code', 'choices']