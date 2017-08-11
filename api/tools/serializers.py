# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from tools.models import Duty

class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Duty
        fields = ['url', 'id', 'username', 'shift', 'content', 'img']