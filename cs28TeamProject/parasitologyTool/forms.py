from django import forms
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label="Title")
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(label="Image", required=False,)

    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

class ResearchPostForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label="Title")
    content = forms.CharField(widget=forms.Textarea)
    images = forms.ImageField(label="Images", required=False,widget=forms.ClearableFileInput(attrs={'multiple': True}))
    files = forms.FileField(label="Files", required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ResearchPost
        fields = ('title', 'content', 'images', 'files')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('clinician', 'Clinician'),
        ('researcher', 'Researcher'),
        ('public', 'Public'),
    ]

    role = forms.CharField(label='Account Type', widget=forms.Select(choices=ROLE_CHOICES))

    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'role',)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=Article.TITLE_MAX_LENGTH, 
                            help_text="Please enter the title of the Article")
    url = forms.URLField(max_length=Article.URL_MAX_LENGTH,
                         help_text="Please enter the URL of the Article.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    picture = forms.ImageField()

    class Meta:
        model = Article
        exclude = ('parasite',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('https://'):
            url = f'https://{url}'
            cleaned_data['url'] = url

        return cleaned_data


class ParasiteForm(forms.ModelForm):
    name = forms.CharField(max_length=Parasite.NAME_MAX_LENGTH,
                           help_text="Please enter the parasite name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    picture = forms.ImageField()
    intro = forms.CharField()

    class Meta:
        model = Parasite
        fields = ('name', 'picture','views','intro')

class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(required = False, label='add comment here')

    class Meta:
        model = Comment
        fields = ('comment_text', )