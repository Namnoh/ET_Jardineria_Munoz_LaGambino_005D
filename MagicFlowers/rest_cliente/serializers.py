from dataclasses import field
from rest_framework import serializers
from app.models import Customer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['custRut', 'custName', 'custLastName', 'custEmail','custTel','custComuna','custAddress']