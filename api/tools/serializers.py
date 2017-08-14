# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from tools.models import Duty, Upload


class UploadSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Upload
        fields = ['url', 'id', 'username', 'file', 'filename', 'archive', 'type', 'size', 'date']


class DutySerializer(serializers.ModelSerializer):
    img = serializers.SlugRelatedField(many=True, queryset=Upload.objects.all(), slug_field='filename')
    #img = UploadSerializer(many=True)

    class Meta:
        model = Duty
        fields = ['url', 'id', 'username', 'shift', 'content', 'img', 'create_time']
        read_only_fields = ('create_time', )
