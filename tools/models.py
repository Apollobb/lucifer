# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from users.models import User
from storage import FileStorage

SHIFT = (
    ("M", u"早班"),
    ("A", u"中班"),
    ("N", u"晚班"),
)

class Duty(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name=u'用户名')
    shift = models.CharField(choices=SHIFT, max_length=30, verbose_name=u'班次')
    content = models.TextField(verbose_name=u'值班内容', null=True, blank=True)
    img = models.ForeignKey('Upload', null=True, blank=True, verbose_name=u'图片')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'项目或任务'
        verbose_name_plural = u'项目或任务'


class Upload(models.Model):
    username = models.CharField(max_length=20, verbose_name=u'上传用户')
    file = models.FileField(upload_to='./',  blank=True, storage=FileStorage(), verbose_name=u'上传文件')
    #archive = models.CharField(max_length=20, verbose_name=u'文件归档')
    type = models.CharField(max_length=20, verbose_name=u'文件类型')
    size = models.CharField(max_length=20, verbose_name=u'文件大小')
    date = models.DateTimeField(auto_now_add=True, verbose_name=u'上传时间')

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = u'文件上传'
        verbose_name_plural = u'文件上传'