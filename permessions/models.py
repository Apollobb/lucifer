# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from utils.permdecode import binEncode
from users.models import User


class MethodChoices(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.code


class Permessions(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=u'权限名称')
    code = models.CharField(max_length=4, default=0000, null=True, blank=True, verbose_name=u'权限代码')
    choices = models.ManyToManyField('MethodChoices', verbose_name=u'选择Method权限')

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        choices = []
        for i in self.choices.all():
            choices.append(str(i))
        self.code = binEncode(choices)
        self.name = '{}-{}'.format(self.name,self.code)
        super(Permessions, self).save(*args, **kwargs)


class ApiPermessions(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=u'权限名称')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'授权用户')
    apiuri = models.CharField(max_length=20, verbose_name=u'授权api')
    perms = models.ForeignKey('Permessions', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'权限')

    def save(self, *args, **kwargs):
        self.name = '{}-{}'.format(self.user,self.apiuri)
        super(ApiPermessions, self).save(*args, **kwargs)