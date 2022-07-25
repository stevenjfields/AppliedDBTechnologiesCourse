from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, mixins, generics
from .models import Provider, Address
from .serializers import AddressSerializer, ProviderSerializer
from django_filters import rest_framework as filters

# Create your views here.
class ProviderFilter(filters.FilterSet):
    class Meta:
        model = Provider
        fields = '__all__'

class AddressFilter(filters.FilterSet):
    class Meta:
        model = Address
        fields = '__all__'
class ProviderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filterset_class = ProviderFilter

class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter

