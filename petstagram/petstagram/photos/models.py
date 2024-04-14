from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.photos.validators import MaxImageSizeValidator
from petstagram.pets.models import Pet

UserModel = get_user_model()


class Photo(models.Model):
    MAX_DESCRIPTION = 300
    MIN_DESCRIPTION = 10
    MAX_LOCATION = 30
    MAX_PHOTO_SIZE = 5.0
    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=(MaxImageSizeValidator(MAX_PHOTO_SIZE),),
        null=False,
        blank=True
    )

    description = models.TextField(
        validators=(
            MinLengthValidator(MIN_DESCRIPTION),
        ),
        max_length=MAX_DESCRIPTION,
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION,
        blank=False,
        null=False,
    )

    date_of_publication = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE
    )
