from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddBulletinForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Bulletin
        fields = ['title', 'content', 'photo', 'cat', 'user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 63:
            raise ValidationError('Длина превышает 63 символа')

        return title