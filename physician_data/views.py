from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, mixins, generics
from .models import Provider, Address
from .serializers import ProviderSerializer

# Create your views here.
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    

