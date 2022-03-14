from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	profile_picture = models.ImageField(upload_to="profile_pictures", default="profile_pictures/default_pic.png")

	ROLE_CHOICES = [
		('clinician', 'Clinician'),
		('researcher', 'Researcher'),
		('public', 'Public'),
		('admin', 'Admin'),
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
	intro = models.CharField(max_length=3000)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Parasite, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	parasite = models.ForeignKey(Parasite, on_delete=models.CASCADE, default=None)
	likes = models.ManyToManyField(User, blank=True, related_name="clinical_likes")
	dislikes = models.ManyToManyField(User, blank=True, related_name="clinical_dislikes")
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
	date_posted = models.DateTimeField(default=timezone.now)

	@property
	def comments(self):
		return self.comment_set.all()
	
	@property
	def images(self):
		return self.clinicalimage_set.all()
	
	@property
	def model(self):
		return self.__class__.__name__

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date_posted',]

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
	#image = models.ImageField(upload_to='clinical_pictures', default=None)
	#file = models.FileField(upload_to='files', default=None)
	likes = models.ManyToManyField(User, blank=True, related_name="likes")
	dislikes = models.ManyToManyField(User, blank=True, related_name="dislikes")
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
	date_posted = models.DateTimeField(default=timezone.now)

	#returns a list of images associated with this post
	@property
	def images(self):
		return self.researchimage_set.all()

	@property
	#returns a list of files associated with this post
	def files(self):
		return self.researchfile_set.all()

	@property
	def comments(self):
		return self.comment_set.all()
	
	@property
	def model(self):
		return self.__class__.__name__

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date_posted',]

class ResearchImage(models.Model):
	research_post = models.ForeignKey(ResearchPost, on_delete=models.CASCADE, default=None)
	image = models.ImageField(upload_to='clinical_pictures', default=None)

class ResearchFile(models.Model):
	research_post = models.ForeignKey(ResearchPost, on_delete=models.CASCADE, default=None)
	file = models.FileField(upload_to='files', default=None)

class ClinicalImage(models.Model):
	clinical_post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
	image = models.ImageField(upload_to='clinical_pictures', default=None, blank=True, null=True)

class Comment(models.Model):
	comment_text = models.TextField()
	research_post = models.ForeignKey(ResearchPost, on_delete = models.CASCADE, default=None, blank=True, null=True)
	clinical_post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None, blank=True, null=True)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
	date_posted = models.DateTimeField(default=timezone.now)

	@property
	def replies(self):
		return self.reply_set.all()

	def __str__(self):
		return self.comment_text

class Reply(models.Model):
	reply_text = models.TextField()
	parent_comment = models.ForeignKey(Comment, on_delete = models.CASCADE)

	def __str__(self):
		return self.reply_text









