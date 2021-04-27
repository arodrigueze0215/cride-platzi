"""Users Serializers."""

#Danjo
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator

#Model
from users.models import User, Profile

#DRF
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

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
        if not user.is_verified:
            raise serializers.ValidationError('Your count is not verified yet. We have sent an email.')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

class UsersignUpSerializer(serializers.Serializer):
    """User sign up Serializers
        Handle the signup request data
    """
    email = serializers.EmailField(
        validators = [UniqueValidator(User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators = [UniqueValidator(User.objects.all())]
    )

    #Phone Number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(
        validators=[phone_regex]
    )

    #Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    #Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        password = data['password']
        password_conf = data['password_confirmation']
        if password != password_conf:
            raise serializers.ValidationError('Passwords do not match.')
        password_validation.validate_password(password)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False)
        Profile.objects.create(user=user)
        return user

