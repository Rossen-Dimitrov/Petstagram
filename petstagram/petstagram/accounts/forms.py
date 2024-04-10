from django import forms
from petstagram.accounts.models import PetstagramUser
from django.contrib.auth import forms as auth_forms


class PetstagramUserCreateForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = PetstagramUser
        fields = ('username', 'email')


class PetstagramUserLoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password'
            }
        )
    )


class PetstagramUserEditForm(forms.ModelForm):
    class Meta():
        model = PetstagramUser
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'gender')
