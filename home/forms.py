from django import forms
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Enquires

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='username')
    first_name = forms.CharField(max_length=50, help_text='first_name')
    last_name = forms.CharField(max_length=50, help_text='last_name')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

def save(self, commit=True):
    user = super(RegisterForm, self).save(commit = False)
    user.email = self.cleaned_data['email']
    if commit:
        user.save()
    return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class EnquiresForm (forms.ModelForm):
    class Meta:
        model = Enquires
        fields = ('receiver', 'sender', 'question')