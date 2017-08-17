# -*- coding: utf-8 -*-
# author: itimor

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class FileStorage(FileSystemStorage):
    def _save(self, name=settings.MEDIA_ROOT, content=settings.MEDIA_URL):
        def path_and_rename():
            def wrapper(instance, filename):
                ext = os.path.splitext(filename)[1]
                filename = "%s-%s%s" % (instance.username, instance.pid, ext)
                archive = instance.archive.split('/')
                if len(archive) > 1:
                    return os.path.join(archive[0], archive[1], filename)
                else:
                    return os.path.join(archive[0], filename)
            return wrapper
        return super(FileStorage, self)._save(path_and_rename, content)