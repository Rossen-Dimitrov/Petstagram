
from django.contrib import admin
from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('', include([
        path('add/', views.photo_add, name='photo add'),
        path('<int:pk>/', views.photo_details, name='photo details'),
        path('<int:pk>/edit/', views.photo_edit, name='photo edit'),
        path('<int:pk>/delete/', views.photo_delete, name='photo delete'),
    ])),

]

