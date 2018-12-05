from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from apiapp.models import info
from apiapp.serializers import infoserializer
# Create your views here.

class testview1(viewsets.ModelViewSet):
    queryset=info.objects.all()
    serializer_class=infoserializer
