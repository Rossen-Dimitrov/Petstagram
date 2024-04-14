
from django.contrib import admin
from django.urls import path, include

from petstagram.photos.views import PhotoAddView, photo_edit, photo_delete, photo_details

urlpatterns = [
    path('', include([
        path('add/', PhotoAddView.as_view(), name='photo add'),
        path('<int:pk>/', photo_details, name='photo details'),
        path('<int:pk>/edit/', photo_edit, name='photo edit'),
        path('<int:pk>/delete/', photo_delete, name='photo delete'),
    ])),

]

