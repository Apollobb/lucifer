# -*- coding: utf-8 -*-
# author: itimor

from django.db import models


class MethodChoices(models.Model):
  name = models.CharField(max_length=30)
  code = models.CharField(max_length=30)


class Profile(models.Model):
  user = models.ForeignKey(User, blank=True, unique=True, verbose_name='user')
  choices = models.ManyToManyField(MethodChoices)