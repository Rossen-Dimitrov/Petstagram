from django.shortcuts import render

from petstagram.pets.models import Pet


def pet_add(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photos_set.all()
    context = {
        "pet": pet,
        "all_photos": all_photos,
        "photos_count": pet.photos_set.count()
    }
    return render(request, 'pets/pet-details-page.html', context=context)


def pet_edit(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')
