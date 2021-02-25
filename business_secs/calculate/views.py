from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import GenericViewSet
from .models import Business_Secs
from .serializers import Business_SecsSerializer


class Business_SecsViewSet(GenericViewSet, CreateModelMixin):
    queryset = Business_Secs.objects.all()
    serializer_class = Business_SecsSerializer
    permission_classes = (DjangoModelPermissions,)
    name = "business-secs"

    def get(self, request, format=None):
        data = request.data
        print(data)