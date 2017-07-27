# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from django.contrib.auth.models import User

ASSET_STATUS = (
    (str(1), u"使用中"),
    (str(2), u"未使用"),
    (str(3), u"故障"),
    (str(4), u"其它"),
)

ASSET_TYPE = (
    (str(1), u"物理机"),
    (str(2), u"虚拟机"),
    (str(3), u"容器"),
    (str(4), u"网络设备"),
    (str(5), u"其他")
)


class Host(models.Model):
    hostname = models.CharField(max_length=50, verbose_name=u"主机名", unique=True)
    ip = models.GenericIPAddressField(u"管理IP", max_length=15)
    other_ip = models.CharField(u"其它IP", max_length=100, null=True, blank=True)
    group = models.ForeignKey('HostGroup', verbose_name=u"设备组", on_delete=models.SET_NULL, null=True, blank=True)
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


class SaltServer(models.Model):
    ip = models.ForeignKey(Host, verbose_name=u'服务器IP')
    port = models.IntegerField(verbose_name=u'端口号')
    apiurl = models.URLField(blank=True, verbose_name=u'api地址')
    username = models.CharField(max_length=20, verbose_name=u'用户名')
    password = models.CharField(max_length=50, verbose_name=u'密码')

    def __unicode__(self):
        return self.ip

    class Meta:
        verbose_name = u'Salt服务器'
        verbose_name_plural = u'Salt服务器列表'


class Upload(models.Model):
    username = models.ForeignKey(User, verbose_name=u'用户')
    headImg = models.FileField(upload_to='upload/', verbose_name=u'文件路径')
    date = models.DateTimeField(auto_now_add=True, verbose_name=u'上传时间')

    def __unicode__(self):
        return self.headImg

    class Meta:
        verbose_name = u'文件上传'
        verbose_name_plural = u'文件上传'
