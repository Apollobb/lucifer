# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from tools.models import Duty, Upload
from users.models import User

class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Duty
        fields = ['url', 'id', 'username', 'shift', 'content', 'img']



class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['url', 'id', 'username', 'file', 'type', 'size', 'date']