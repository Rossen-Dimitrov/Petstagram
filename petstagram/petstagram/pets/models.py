from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    PET_MAX_NAME = 30

    name = models.CharField(
        max_length=PET_MAX_NAME,
        blank=False,
        null=False,
    )
    personal_pet_photo = models.URLField(
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        editable=False,
        unique=True,
        blank=True,
        null=False,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
