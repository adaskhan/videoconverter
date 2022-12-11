from django import forms

from .models import Convert


class ConvertForm(forms.ModelForm):
    '''Форма подписки по email'''
    class Meta:
        model = Convert
        fields = ['yt_url', 'email']
