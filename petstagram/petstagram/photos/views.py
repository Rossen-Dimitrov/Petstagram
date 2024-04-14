from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic as views

from petstagram.photos.forms import PhotoEditForm, PhotoCreateForm, PhotoDeleteForm
from petstagram.photos.models import Photo
from django.contrib.auth.mixins import LoginRequiredMixin

UserModel = get_user_model()


class PhotoAddView(LoginRequiredMixin, views.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoCreateForm

    def get_success_url(self):
        return reverse('photo details', kwargs={
            'pk': self.object.pk
        })

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save
    #     return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


@login_required
def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.photolike_set.all()
    comments = photo.photocomment_set.all()

    if photo.photolike_set.filter(user=request.user).exists():
        photo.liked_by_user = photo.photolike_set
    context = {
        'photo': photo,
        'comments': comments,
        'likes': likes,
        'owner': photo.user
    }
    return render(request, 'photos/photo-details-page.html', context=context)


@login_required
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


@login_required
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
