from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Parasite)
admin.site.register(Article)
admin.site.register(ResearchPost)
admin.site.register(ResearchImage)
admin.site.register(Comment)
admin.site.register(ClinicalImage)
admin.site.register(Reply)