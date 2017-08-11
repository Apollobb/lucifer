# -*- coding: utf-8 -*-
# author: itimor

from django.db import models

SHIFT = (
    ("M", u"早班"),
    ("A", u"中班"),
    ("N", u"晚班"),
)

class Duty(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name=u'用户名')
    shift = models.CharField(choices=SHIFT, max_length=30, verbose_name=u'班次')
    content = models.TextField(verbose_name=u'值班内容', null=True, blank=True)
    img = models.ImageField(upload_to='img/', verbose_name=u'文件路径')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'项目或任务'
        verbose_name_plural = u'项目或任务'