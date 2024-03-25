from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoEditForm, PhotoCreateForm, PhotoDeleteForm
from petstagram.photos.models import Photo


def photo_add(request):
    form = PhotoCreateForm()
    if request.method == 'POST':
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return redirect('photo details', pk=photo.pk)

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context=context)


def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.photolike_set.all()
    comments = photo.photocomment_set.all()
    context = {
        'photo': photo,
        'comments': comments,
        'likes': likes
    }
    return render(request, 'photos/photo-details-page.html', context=context)


def photo_edit(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details', pk=pk)

    context = {
        'form': form,
        "pk": pk
    }

    return render(request, 'photos/photo-edit-page.html', context=context)


def photo_delete(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'POST':
        photo.delete()
        return redirect('home', pk=1)

    form = PhotoDeleteForm(instance=photo)

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'photos/photo-delete-page.html', context=context)
