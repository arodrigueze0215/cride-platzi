"""Users views """

#DRF
from rest_framework.views import APIView
from rest_framework import status

#serializer
from cride.serializers.users import (
    UserModelSerializer,
    UserLoginSerializer,
    UsersignUpSerializer,
)
from rest_framework.response import Response

class UserLoginAPIView(APIView):
    """User Login APIView."""

    def post(self, request, *args, **kargs):
        """Handle HTTP POST request"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status= status.HTTP_201_CREATED)

class UserSignUpAPIView(APIView):
    """User sign up APIView"""

    def post(self, request, *args, **kargs):
        """Handle HTTP POST request"""
        serializer = UsersignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status= status.HTTP_201_CREATED)
