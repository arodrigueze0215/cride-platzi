"""Users Serializers."""

#Danjo
from django.contrib.auth import authenticate

#Model
from users.models import User

#DRF
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email' )

class UserLoginSerializer(serializers.Serializer):
    """ User Login Serializer.
        Handle the login request data
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials.')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
