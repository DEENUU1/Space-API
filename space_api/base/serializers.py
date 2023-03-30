from rest_framework import serializers
from .models import Planet, System, Galaxy, Rocket, Mission


class PlanetSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Planet model
    Attributes:
        Meta (class): A nested class which specifies the model
        and fields to be use fot serialization.
    """
    image = serializers.ImageField(max_length=None, use_url=True)

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
    image = serializers.ImageField(max_length=None, use_url=True)

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

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Galaxy
        fields = '__all__'


class RocketSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Rocket model
    Attributes:
        Meta (class): A nested class which specifies the model
        and fields to be use fot serialization.
    """
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Rocket
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Mission model
    Attributes:
        Meta (class): A nested class which specifies the model
        and fields to be use fot serialization.
    """
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Mission
        fields = '__all__'
