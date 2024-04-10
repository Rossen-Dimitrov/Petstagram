from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.forms import PhotoCommentForm, SearchForm
from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


def home(request):
    all_photos = Photo.objects.all()
    comment_form = PhotoCommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        "all_photos": all_photos,
        'comment_form': comment_form,
        'search_form': search_form
    }
    return render(request, template_name='common/home-page.html', context=context)


@login_required
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


@login_required
def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_REFERER'] + resolve_url('photo details', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


@login_required
def add_comment(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.filter(pk=photo_id).get()
        form = PhotoCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()
        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
