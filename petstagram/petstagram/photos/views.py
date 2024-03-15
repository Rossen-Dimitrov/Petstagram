from django.shortcuts import render

from petstagram.photos.models import Photo


def photo_add(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.photolike_set.all()
    comments = photo.photocomment_set.all()
    context = {
        'photo': photo,
        'comments': comments,
        'likes': likes
    }
    return render(request, 'photos/photo-details-page.html', context=context)


def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
