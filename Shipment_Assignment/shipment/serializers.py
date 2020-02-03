from rest_framework import serializers
from .models import Shipment,ClientCredential,Order

class ClientCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCredential
        fields = "__all__"

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


