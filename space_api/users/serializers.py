from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .email import send_email


class GetTokenSerializer(serializers.ModelSerializer):
    """
    This serializer class is a Django REST Framework serializer that is used to serialize user data to and from
    JSON format. It includes a build in User model and the email field to be serialized.
    """

    class Meta:
        model = User
        fields = ['email']

    def create(self, validated_data):
        """
        This` method creates a new user instance based on the validated data passed into it as
        the `validate_data` parameter.
        """
        user = User(email=validated_data['email'])
        user.save()
        token = Token.objects.create(user=user)
        send_email(
            "Token",
            "email_token.html",
            token,
            user.email
        )
        return user
