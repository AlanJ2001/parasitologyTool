from django import forms
from django.contrib.auth.models import User
from .models import Post, UserProfile

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Title")
    content = forms.CharField(help_text="Data")

    class Meta:
        model = Post
        fields = ('title', 'content',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)