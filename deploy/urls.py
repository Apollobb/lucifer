# -*- coding: utf-8 -*-
# author: itimor

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from deploy import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_auth.views import PasswordChangeView

from api.hosts.views import HostViewSet, HostGroupViewSet, SaltServerViewSet, UploadViewSet
from api.jobs.views import JobsViewSet, JobGroupViewSet
from api.users.views import UserViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'hosts', HostViewSet)
router.register(r'hostgroups', HostGroupViewSet)
router.register(r'salt', SaltServerViewSet)
router.register(r'upload', UploadViewSet)
router.register(r'jobs', JobsViewSet)
router.register(r'jobgroup', JobGroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api/', include(router.urls)),

                  # 用户认证
                  url(r'^api/changepasswd/', PasswordChangeView.as_view(), name='changepasswd'),
                  url(r'^api-token-auth/', obtain_jwt_token, name='rest_framework_token'),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
