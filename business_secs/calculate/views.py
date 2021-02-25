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

    def post(self, request, format=None):
        print(request.GET)
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)