# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from utils.permdecode import binEncode
from users.models import User
from multiselectfield import MultiSelectField

METHOD_CHOICES = (
    ('get','get'),
    ('post','post'),
    ('put','put'),
    ('delete','delete')
)

class ApiPermessions(models.Model):
    name = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name=u'权限名称')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'授权用户')
    apiuri = models.CharField(max_length=20, verbose_name=u'授权api')
    code = models.CharField(max_length=4, default=0000, null=True, blank=True, verbose_name=u'权限代码')
    choices = MultiSelectField(choices=METHOD_CHOICES)

    def save(self, *args, **kwargs):
        choices = list(self.choices)
        self.code = binEncode(choices)
        self.name = '{}{}'.format(self.user, self.apiuri.replace('/','-'))
        super(ApiPermessions, self).save(*args, **kwargs)