from rest_framework import serializers
from .models import Planet, System, Galaxy


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


class SystemSerializer(serializers.ModelSerializer):
    """
    A serializer class for the System model
    Attributes:
        Meta (class): A nested class which specifies the model
        and fields to be use fot serialization.
    """
    class Meta:
        model = System
        fields = '__all__'


class GalaxySerializer(serializers.ModelSerializer):
    """
    A serializer class for the Galaxy model
    Attributes:
        Meta (class): A nested class which specifies the model
        and fields to be use fot serialization.
    """
    class Meta:
        model = Galaxy
        fields = '__all__'
