from rest_framework import routers, serializers, viewsets
from .models import Provider, Address

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'