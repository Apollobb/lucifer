# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import permissions
from permessions.models import ApiPermessions

class UserPerms(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        apiperm = ApiPermessions.objects.get(user=request.user)

        print(request.path)
        if request.method in permissions.SAFE_METHODS:
            return True

        return True
