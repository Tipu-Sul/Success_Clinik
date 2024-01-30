from django.shortcuts import render
from rest_framework import viewsets
from. import models
from. import serializer
# Create your views here.
class ContactUsViewset(viewsets.ModelViewSet):
    queryset=models.ContactUs.objects.all()
    serializer_class=serializer.ContactUsSerializer
