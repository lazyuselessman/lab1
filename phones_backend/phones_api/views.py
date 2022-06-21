from django.shortcuts import render
from rest_framework import viewsets

from phones_api.serializers import NumberSerializer, PhoneSerializer, UserSerializer
from phones_api.models import Number, Phone, User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

