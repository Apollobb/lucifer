# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from hosts.models import Host
from users.models import User


class SaltServer(models.Model):
    ip = models.ForeignKey(Host, verbose_name=u'服务器IP')
    port = models.IntegerField(verbose_name=u'端口号')
    apiurl = models.URLField(max_length=20, null=True, blank=True, verbose_name=u'salt API地址')
    username = models.CharField(max_length=20, verbose_name=u'用户名')
    password = models.CharField(max_length=50, verbose_name=u'密码')

    def __unicode__(self):
        return self.ip

    def save(self, *args, **kwargs):
        self.apiurl = 'http://{}:{}'.format(self.ip, self.port)
        super(SaltServer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'Salt服务器'
        verbose_name_plural = u'Salt服务器列表'


class SaltCmdrun(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    cmd = models.CharField(max_length=500, verbose_name=u'命令')
    hosts = models.ManyToManyField(Host, null=True, blank=True, verbose_name=u'主机')

    class Meta:
        verbose_name = u'Salt cmdrun'
        verbose_name_plural = u'Salt cmdrun'
