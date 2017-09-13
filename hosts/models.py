# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from users.models import User

ASSET_STATUS = (
    ('used', u"使用中"),
    ('noused', u"未使用"),
    ('broken', u"故障"),
    ('other', u"其它"),
)

ASSET_TYPE = (
    ('physical', u"物理机"),
    ('virtual', u"虚拟机"),
    ('container', u"容器"),
    ('network', u"网络设备"),
    ('other', u"其他设备")
)


class Host(models.Model):
    hostname = models.CharField(max_length=50, verbose_name=u"主机名", unique=True)
    ip = models.GenericIPAddressField(u"管理IP", unique=True, max_length=15)
    other_ip = models.CharField(u"其它IP", max_length=100, null=True, blank=True)
    group = models.ManyToManyField('HostGroup', verbose_name=u"组", null=True, blank=True)
    asset_type = models.CharField(u"设备类型", choices=ASSET_TYPE, max_length=30, null=True, blank=True)
    status = models.CharField(u"设备状态", choices=ASSET_STATUS, max_length=30, null=True, blank=True)
    os = models.CharField(u"操作系统", max_length=100, null=True, blank=True)
    cpu_model = models.CharField(u"CPU型号", max_length=100, null=True, blank=True)
    cpu_num = models.CharField(u"CPU数量", max_length=100, null=True, blank=True)
    memory = models.CharField(u"内存大小", max_length=30, null=True, blank=True)
    disk = models.CharField(u"硬盘信息", max_length=255, null=True, blank=True)
    memo = models.TextField(u"备注信息", max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.hostname

    class Meta:
        verbose_name = u'服务器'
        verbose_name_plural = u'服务器列表'


class HostGroup(models.Model):
    name = models.CharField(u"组名", max_length=30, unique=True)
    desc = models.CharField(u"描述", max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'服务器组'
        verbose_name_plural = u'服务器组'