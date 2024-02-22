from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Registration
from .serializers import RegistrationSerializer
from rest_framework import filters

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'date_of_birth']
