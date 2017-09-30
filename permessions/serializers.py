# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from permessions.models import METHOD_CHOICES, ApiPermessions


class ApiPermessionsSerializer(serializers.ModelSerializer):
    choices = serializers.MultipleChoiceField(choices=METHOD_CHOICES, default='get')
    class Meta:
        model = ApiPermessions
        fields = ['url', 'id', 'name', 'user', 'apiuri', 'code', 'choices']