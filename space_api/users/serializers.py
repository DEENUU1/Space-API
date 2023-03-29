from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class GetTokenSerializer(serializers.ModelSerializer):
    """
    Docstring
    """

    class Meta:
        model = User
        fields = ['email']

    def create_user(self, validate_data):
        """
        :param validate_data:
        :return:
        """
        user = User(email=validate_data['email'])
        user.save()
        token = Token.objects.create(usesr=user)

        return user
