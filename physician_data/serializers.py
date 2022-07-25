from rest_framework import routers, serializers, viewsets
from .models import Provider, Address
from django_restql.mixins import DynamicFieldsMixin

class ProviderSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'