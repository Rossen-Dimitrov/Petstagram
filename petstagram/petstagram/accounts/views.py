from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.templatetags.static import static
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from petstagram.accounts.forms import (
    PetstagramUserCreateForm, PetstagramUserLoginForm, PetstagramUserEditForm,
)
from petstagram.accounts.models import PetstagramUser
from django.views.generic.edit import UpdateView, DeleteView

from petstagram.photos.models import Photo

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)

        # user = self.object
        # login(self.request, user)

        login(self.request, self.object)

        return result

    # def get_success_url(self):
    #     return self.request.POST.get('next', self.success_url)
    #


class UserLogin(auth_views.LoginView):
    form_class = PetstagramUserLoginForm
    template_name = 'accounts/login-page.html'
    # success_url = reverse_lazy('home') # using global login redirect


def logout_view(request):
    logout(request)
    return redirect('home')


class ProfileDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = "accounts/profile-details-page.html"
    model = UserModel

    profile_img = static('/images/person.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_img

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['user'] = PetstagramUser.objects.all()
        context['profile_img'] = self.get_profile_image()
        context['pets'] = self.request.user.pet_set.all()
        context['photos'] = self.request.user.photo_set.all()

        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = PetstagramUserEditForm
    # queryset = UserModel.objects.all()
    template_name = "accounts/profile-edit-page.html"

    # fields = ("first_name", "last_name", "profile_picture")
    def get_success_url(self):
        return reverse("user profile details", kwargs={
            "pk": self.object.pk,
        })


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'

    # def post(self, *args, pk):
    #     self.request.user.delete()

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('home')
        self.object.delete()
        return redirect(success_url)

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #
    #     # Delete user activity (replace with your own logic for deleting activity)
    #     self.object.posts.all().delete()
    #     # self.object.comments.all().delete()
    #     # Add more lines to delete other related activity if needed
    #
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #
    #     return redirect(success_url)
