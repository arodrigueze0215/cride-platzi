"""User models"""

#django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#uitls
from uitls.models import CRideModel

class User(CRideModel, AbstractUser):
    """
    Extends from django's Abstrac User, The goal is change the username field to
    email field and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique = True,
        error_messages = {
            'unique': 'A user with the email allready exists!'
        }
    )
    
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default = True,
        help_text = 'Client are the main type user'
    )
    is_verified = models.BooleanField(
        'verified',
        default = False,
        help_text = 'Set to true when the user has been verified through its email'
    )

    def __str__(self):
        """Return Username"""
        return self.username

    def get_short_name(self):
        """Return username"""
        return self.username