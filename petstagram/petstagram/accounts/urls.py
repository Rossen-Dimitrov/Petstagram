
from django.urls import path, include

from petstagram.accounts import views
from petstagram.accounts.views import (
    UserRegisterView, UserLogin, ProfileEditView, ProfileDetailsView, logout_view, ProfileDeleteView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user register'),
    path('login/', UserLogin.as_view(), name='user login'),
    path('logout/', logout_view, name='user logout'),
    path('<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='user profile details'),
        path('edit/', ProfileEditView.as_view(), name='user edit profile'),
        path('delete/', ProfileDeleteView.as_view(), name='user delete profile'),
    ])),
]
