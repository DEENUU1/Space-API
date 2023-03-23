from rest_framework import serializers
from .models import Planet


class PlanetSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Planet model
    Attributes:
        Meta (class): A nested class which specifies the model
        and fields to be use fot serialization.
    """
    class Meta:
        model = Planet
        fields = '__all__'
