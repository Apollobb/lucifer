# -*- coding: utf-8 -*-
# author: itimor

from users.models import Group, User, Role
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, RoleSerializer
from filters import UserFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    ordering_fields = ('-create_date',)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


from rest_framework import mixins, generics
class CreateUserView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)