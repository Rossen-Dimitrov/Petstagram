from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy
from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


def home(request):
    context = {
        "all_photos": Photo.objects.all()
    }
    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = PhotoLike.objects.filter(to_photo=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        PhotoLike.objects.create(
            to_photo=photo
        )

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_REFERER'] + resolve_url('photo details', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')
