# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from permessions.models import MethodChoices, Permessions

class PermessionsSerializer(serializers.ModelSerializer):
    choices = serializers.SlugRelatedField(many=True, queryset=MethodChoices.objects.all(), slug_field='code')
    class Meta:
        model = Permessions
        fields = ['url', 'id', 'name', 'apiuri', 'code', 'choices']


class MethodChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodChoices
        fields = ['url', 'id', 'name', 'code']