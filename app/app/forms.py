from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100, help_text='Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = get_user_model()
        fields = ('name', 'email')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 3}}
