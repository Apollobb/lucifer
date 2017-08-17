# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from filesize import convert_size
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
    images = models.ManyToManyField('Upload', null=True, blank=True, verbose_name=u'图片')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'值班交接'
        verbose_name_plural = u'值班交接'

import os
class Upload(models.Model):
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = os.path.splitext(filename)[1]
            filename = "%s-%s%s" % (instance.username, instance.pid, ext)
            archive = instance.archive.split('/')
            if len(archive)>1:
                return os.path.join(path, archive[0], archive[1], filename)
            else:
                return os.path.join(path, archive[0], filename)
        return wrapper

    username = models.CharField(max_length=20, verbose_name=u'上传用户')
    pid = models.IntegerField(u'图片id', null=True, blank=True)
    file = models.FileField(upload_to=path_and_rename('./'), blank=True, verbose_name=u'上传文件')
    archive = models.CharField(max_length=101, default=u'其他', null=True, blank=True, verbose_name=u'文件归档')
    filepath = models.CharField(max_length=201, null=True, blank=True, verbose_name=u'文件名')
    type = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'文件类型')
    size = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'文件大小')
    date = models.DateTimeField(auto_now_add=True, verbose_name=u'上传时间')

    def save(self, *args, **kwargs):
        self.size = '{}'.format(convert_size(self.file.size))
        ext = os.path.splitext(self.file.name)[1]
        self.filepath = '{}/{}-{}{}'.format(self.archive, self.username, self.pid, ext)
        super(Upload, self).save(*args, **kwargs)


    def __unicode__(self):
        return u'{}'.format(self.filepath)

    class Meta:
        verbose_name = u'文件上传'
        verbose_name_plural = u'文件上传'
