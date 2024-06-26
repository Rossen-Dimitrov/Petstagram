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
        max_length=1,
        default='X'
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name

        return self.username


