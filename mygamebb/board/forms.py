from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddBulletinForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Bulletin
        fields = ['title', 'content', 'cat',  'user']


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 63:
            raise ValidationError('Длина превышает 63 символа')

        return title

class AddReplyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reply'].empty_label = "Категория не выбрана"

    class Meta:
        model = Comment
        fields = ['reply', 'user', 'bulletin']


    def clean_reply(self):
        reply = self.cleaned_data['reply']
        if len(reply) > 255:
            raise ValidationError('Длина превышает 255 символов')

        return reply

class ConfirmCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['is_accept']



