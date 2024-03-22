from django import forms


class PhotoBaseForm(forms.ModelForm):
    pass


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    pass


class PhotoDeliteForm(PhotoBaseForm):
    pass
