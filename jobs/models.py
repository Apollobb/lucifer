# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from hosts.models import Host

DEPLOY_STATUS = (
    ("unexecuted", u"未执行"),
    ("deploy", u"发布中"),
    ("succed", u"发布成功"),
    ("failed", u"发布失败"),
)


class Jobs(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=u'任务名')
    hosts = models.ManyToManyField(Host, null=True, blank=True, verbose_name=u'被发布的主机')
    group = models.ForeignKey('JobGroup', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'任务组')
    jobs_type = models.CharField(u"项目语言类型", max_length=30, null=True, blank=True)
    code_repo = models.CharField(u"代码仓库", max_length=30, null=True, blank=True)
    code_url = models.CharField(u"代码地址", max_length=100, null=True, blank=True)
    code_branch = models.CharField(max_length=20, verbose_name=u'代码分支', default='master', null=True, blank=True)
    deploy_env = models.CharField(u"发布环境", max_length=100, null=True, blank=True)
    deploy_script = models.TextField(verbose_name=u'发布脚步', null=True, blank=True)
    deploy_test = models.TextField(verbose_name=u'发布测试', null=True, blank=True)
    deploy_status = models.CharField(u"发布状态", choices=DEPLOY_STATUS, default=DEPLOY_STATUS[0][0], max_length=30, null=True, blank=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'发布时间', null=True)
    cost_time = models.DateTimeField(u'发布耗时', null=True)
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