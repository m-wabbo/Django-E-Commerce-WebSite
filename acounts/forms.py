from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ['username','email','password']

class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['pic','name','country','phone','bdate']


class UserEditForm(forms.ModelForm):
    class Meta:
        model =	User
        fields = ['username','email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model =	Profile
        fields = ['pic','name','country','phone','bdate']
