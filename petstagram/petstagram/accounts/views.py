from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, logout
from petstagram.accounts.forms import PetstagramUserCreateForm, PetstagramUserLoginForm
from petstagram.accounts.models import PetstagramUser


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


def user_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def user_edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def user_delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
