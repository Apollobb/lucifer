# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from tools.models import Duty, Upload


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['url', 'id', 'username', 'file', 'filename', 'archive', 'type', 'size', 'date']


class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Duty
        fields = ['url', 'id', 'username', 'shift', 'content', 'images', 'create_time']
        read_only_fields = ('create_time', )
