"""User Urls"""

#Django
from django.urls import path

#Views
from cride.users.views.users import (
    UserLoginAPIView,
    UserSignUpAPIView
)

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),

]
