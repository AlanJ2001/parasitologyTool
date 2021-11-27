from django.contrib import admin
from .models import *
# Register your models here.


class ParasiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Post)
admin.site.register(UserProfile)
<<<<<<< Updated upstream
admin.site.register(Parasite)
admin.site.register(Article)
=======
admin.site.register(Parasite, ParasiteAdmin)
>>>>>>> Stashed changes
