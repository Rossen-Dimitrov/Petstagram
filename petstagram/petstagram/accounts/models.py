from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class PetstagramUser(AbstractUser):
    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 2

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Do not show')
    )

    email = models.EmailField(
        unique=True
    )
    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH)
        ]
    )
    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH)
        ]
    )
    profile_picture = models.URLField(
        blank=True,
        null=True
    )

    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=1
    )
