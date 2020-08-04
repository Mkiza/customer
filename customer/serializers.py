#Import the Customer model
#Import the REST Framework serializer
#Create a new class that links the Customer with its serializer

from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'phone')
