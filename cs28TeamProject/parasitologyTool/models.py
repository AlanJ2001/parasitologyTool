from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	profile_picture = models.ImageField(upload_to="profile_pictures", default="profile_pictures/default_pic.png")

	ROLE_CHOICES = [
		('clinician', 'Clinician'),
		('researcher', 'Researcher'),
		('public', 'Public'),
	]

	role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Public')

	@property
	def username(self):
		return self.user.username
		
	def __str__(self):
		return self.user.username

class Parasite(models.Model):
	NAME_MAX_LENGTH = 128
	name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
	views = models.IntegerField(default=0)
	picture = models.ImageField(upload_to='parasite_pic')


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Parasite, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	parasite = models.ForeignKey(Parasite, on_delete=models.CASCADE, default=None)
	image = models.ImageField(upload_to='clinical_pictures', default=None)
	#date_posted = models.DateTimeField(auto_now_add=True)
	#author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Article(models.Model):
	TITLE_MAX_LENGTH = 128
	URL_MAX_LENGTH = 200
	
	parasite = models.ForeignKey(Parasite, on_delete=models.CASCADE, default=None)
	title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True)
	url = models.URLField(max_length=URL_MAX_LENGTH)
	views = models.IntegerField(default=0)
	picture = models.ImageField(upload_to='article_pic')

	def __str__(self):
		return self.title

class ResearchPost(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	parasite = models.ForeignKey(Parasite, on_delete=models.CASCADE, default=None)
	image = models.ImageField(upload_to='clinical_pictures', default=None)
	file = models.FileField(upload_to='files', default=None)

	def __str__(self):
		return self.title











