# -*- coding: utf-8 -*-
# author: itimor

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os, time, random

class FileStorage(FileSystemStorage):
    def _save(self, name=settings.MEDIA_ROOT, content=settings.MEDIA_URL):
        # 文件扩展名
        fileext = os.path.splitext(name)[1]
        # 文件目录
        d = os.path.dirname(name)
        # 定义文件名，年月日时分秒随机数
        fntime = time.strftime('%Y%m%d%H%M%S') + '_%d' % random.randint(0, 100)
        # 重写合成文件名
        upload_filename = os.path.join(d, fntime + fileext)
        # 调用父类方法
        return super(FileStorage, self)._save(upload_filename, content)