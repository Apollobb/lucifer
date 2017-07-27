from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from deploy import settings
from django.conf.urls.static import static

from api.hosts.views import HostViewSet, HostGroupViewSet, SaltServerViewSet, UploadViewSet
from api.jobs.views import JobsViewSet, JobGroupViewSet

router = DefaultRouter()
router.register(r'host', HostViewSet)
router.register(r'hostgroup', HostGroupViewSet)
router.register(r'salt', SaltServerViewSet)
router.register(r'upload', UploadViewSet)
router.register(r'jobs', JobsViewSet)
router.register(r'jobgroup', JobGroupViewSet)


urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api/', include(router.urls)),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)