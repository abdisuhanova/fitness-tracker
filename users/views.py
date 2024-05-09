from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializers


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)