from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [ 'email', 'username','password1', 'password2']


class UploadForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('snapshot', 'title', 'url', 'description', 'technologies',)
        exclude = ["date_posted", "developer"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']