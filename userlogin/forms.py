"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import offers


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Your last name.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class addOfferForm(forms.ModelForm):
    # forms.offering_text.required=True 
    # offering_text.help_text='Please describe your offer.'
    # required=True, help_text='Please add an amount of time in hours'
    offering_text = forms.CharField(max_length=500, required=True, help_text='Please describe your offer.')

    class Meta:
        model = offers
        fields = ('offering_text', 'offering_time',)

