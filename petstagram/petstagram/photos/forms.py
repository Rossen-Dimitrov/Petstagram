from django import forms
from django.core.exceptions import ValidationError

from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']


class PhotoDeleteForm(PhotoBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #     return self.instance
    #
    # def clean_tagged_pets(self):
    #     tagged_pets = self.cleaned_data['tagged_pets']
    #     if tagged_pets:
    #         raise ValidationError('Pets are tagged in this photo')
