from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	profile_picture = models.ImageField(upload_to="profile_pictures", default="profile_pictures/default_pic.png")

	ROLE_CHOICES = [
		('Clinician', 'Clinician'),
		('Researcher', 'Researcher'),
	]

	Role = models.CharField(max_length=50, choices=ROLE_CHOICES)

	@property
	def username(self):
		return self.user.username
		
	def __str__(self):
		return self.user.username