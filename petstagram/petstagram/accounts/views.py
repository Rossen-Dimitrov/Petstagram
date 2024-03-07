from django.shortcuts import render


def user_register(request):
    return render(request, template_name='accounts/register-page.html')


def user_login(request):
    return render(request, template_name='accounts/login-page.html')


def user_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def user_edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def user_delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
