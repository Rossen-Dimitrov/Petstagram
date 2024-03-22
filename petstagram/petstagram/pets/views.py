from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeliteForm
from petstagram.pets.models import Pet


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        "pet": pet,
        "all_photos": all_photos,
        "photos_count": pet.photo_set.count()
    }
    return render(request, 'pets/pet-details-page.html', context=context)


def pet_add(request):
    form = PetCreateForm(request.GET)
    if request.method == 'POST':
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user profile details", pk=1)
    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context=context)


def pet_edit(request, username, pet_slug):
    pet = (Pet.objects
           .filter(slug=pet_slug)
           .get())

    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet details", username, pet_slug)

    context = {
        'form': form,
        'slug': pet_slug,
        'username': username
    }

    return render(request, 'pets/pet-edit-page.html', context=context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    if request.method == 'POST':
        pet.delete()
        return redirect("user profile details", pk=1)

    form = PetDeliteForm(instance=pet)

    context = {
        'form': form,
        'username': username,
        'slug': pet_slug
    }

    return render(request, 'pets/pet-delete-page.html', context=context)
