from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import GenericViewSet


class Business_SecsViewSet(GenericViewSet, CreateModelMixin):
    queryset = Business_Secs.objects.all()
    serializer_class = Business_SecsSerializer
    permission_classes = (DjangoModelPermissions,)
