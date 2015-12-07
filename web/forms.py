from django import forms
from django.forms import Form


class NewShortURL(Form):

    url = forms.CharField(label='URL to short', max_length=2000, required=True)
