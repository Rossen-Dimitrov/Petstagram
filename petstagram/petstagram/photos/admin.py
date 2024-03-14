from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'pets')

    @staticmethod
    def pets(photo_obj):
        tagged_pets = photo_obj.tagged_pets.all()
        if tagged_pets:
            print(tagged_pets)
            return ', '.join(pet.name for pet in tagged_pets)
        else:
            return 'No tagged pets'
