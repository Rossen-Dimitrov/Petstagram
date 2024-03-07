
from django.contrib import admin
from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.user_register, name='user register'),
    path('login/', views.user_login, name='user login'),
    path('<int:pk>/', include([
        path('', views.user_profile_details, name='user profile details'),
        path('edit/', views.user_edit_profile, name='user edit profile'),
        path('delete/', views.user_delete_profile, name='user delete profile'),
    ])),
]
