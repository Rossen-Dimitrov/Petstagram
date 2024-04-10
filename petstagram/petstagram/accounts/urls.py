
from django.urls import path, include

from petstagram.accounts import views
from petstagram.accounts.views import (
    UserRegisterView, UserLogin,
    user_profile_details, user_delete_profile, user_edit_profile, logout_view)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user register'),
    path('login/', UserLogin.as_view(), name='user login'),
    path('logout/', logout_view, name='user logout'),
    path('<int:pk>/', include([
        path('', user_profile_details, name='user profile details'),
        path('edit/', user_edit_profile, name='user edit profile'),
        path('delete/', user_delete_profile, name='user delete profile'),
    ])),
]
