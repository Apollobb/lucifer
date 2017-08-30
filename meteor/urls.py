# -*- coding: utf-8 -*-
# author: itimor

from django.conf.urls import url, include
from django.contrib import admin
from meteor import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_auth.views import PasswordChangeView
from api.router import router
from django.views.generic.base import TemplateView

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api/', include(router.urls)),

                  # 用户认证
                  url(r'^api/changepasswd/', PasswordChangeView.as_view(), name='changepasswd'),
                  url(r'^api-token-auth/', obtain_jwt_token, name='rest_framework_token'),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^$', TemplateView.as_view(template_name="index.html")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
