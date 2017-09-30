# -*- coding: utf-8 -*-
# author: itimor

from rest_framework.routers import DefaultRouter

from hosts.views import HostViewSet, HostGroupViewSet
from jobs.views import JobsViewSet, JobGroupViewSet
from salts.views import SaltServerViewSet, SaltCmdrunViewSet, SaltStateViewSet
from tools.views import DutyViewSet, UploadViewSet
from users.views import UserViewSet, GroupViewSet, RoleViewSet
from permessions.views import ApiPermessionsViewSet

router = DefaultRouter()
router.register(r'hosts', HostViewSet)
router.register(r'hostgroups', HostGroupViewSet)
router.register(r'saltserver', SaltServerViewSet)
router.register(r'saltcmdrun', SaltCmdrunViewSet)
router.register(r'saltstate', SaltStateViewSet)
router.register(r'upload', UploadViewSet)
router.register(r'jobs', JobsViewSet)
router.register(r'jobgroups', JobGroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'dutys', DutyViewSet)

router.register(r'apiperms', ApiPermessionsViewSet)