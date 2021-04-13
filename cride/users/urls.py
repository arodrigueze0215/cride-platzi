"""User Urls"""

#Django
from django.urls import path

#Views
from cride.users.views.users import UserLoginAPIView

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),

]
