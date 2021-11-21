from django import forms
from django.contrib.auth.models import User
from .models import Post, UserProfile , Article

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

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=Article.TITLE_MAX_LENGTH, 
                            help_text="Please enter the title of the Article")
    url = forms.URLField(max_length=Article.URL_MAX_LENGTH,
                         help_text="Please enter the URL of the Article.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Article
        exclude = ('parasite',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data