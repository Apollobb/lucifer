# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from hosts.models import Host

JOBS_TYPE = (
    (str(1), u"php"),
    (str(2), u"java"),
    (str(3), u"net"),
    (str(4), u"python"),
    (str(5), u"node")
)

REPO_TYPE = (
    (str(1), u"git"),
    (str(2), u"svn"),
    (str(3), u"ftp"),
)


class Jobs(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'任务名')
    hosts = models.ManyToManyField(Host, verbose_name=u'被发布的主机')
    group = models.ForeignKey('JobGroup', verbose_name=u'任务组')
    jobs_type = models.CharField(u"项目语言类型", choices=JOBS_TYPE, max_length=30, null=True, blank=True)
    code_repo = models.CharField(u"代码仓库", choices=REPO_TYPE, max_length=30, null=True, blank=True)
    code_url = models.CharField(u"代码地址", choices=REPO_TYPE, max_length=30, null=True, blank=True)
    code_branch = models.CharField(max_length=20, verbose_name=u'代码分支', null=True, blank=True)
    code_version = models.CharField(max_length=20, verbose_name=u'代码版本', null=True, blank=True)
    deploy_script = models.TextField(verbose_name=u'发布脚步', null=True, blank=True)
    deploy_test = models.TextField(verbose_name=u'发布测试', null=True, blank=True)
    desc = models.CharField(u"项目描述", max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'项目或任务'
        verbose_name_plural = u'项目或任务'


class JobGroup(models.Model):
    name = models.CharField(u"组名", max_length=30, unique=True)
    desc = models.CharField(u"描述", max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'项目组'
        verbose_name_plural = u'项目组'