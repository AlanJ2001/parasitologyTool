from django.conf.urls import url
from django.urls import path
from parasitologyTool import views
from django.urls import path

app_name = 'parasitologyTool'

urlpatterns = [
<<<<<<< Updated upstream
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_post/', views.add_post, name='add_post'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('public_content/', views.public_content, name='public_content'),
    path('public_content/<int:parasite_id>/add_article/',views.add_article, name='add_article'),
    path('public_content/<int:parasite_id>/', views.public_parasite_page, name = 'public_parasite_page')
=======
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'add_post/', views.add_post, name='add_post'),
    url(r'register/', views.register, name='register'),
    url(r'login/', views.user_login, name='login'),
    url(r'logout/', views.user_logout, name='logout'),
    path('public_content/', views.public_content, name='public_content'),
    #url(r'add_article/',views.add_article, name='add_article'),
    path('public_content/parasite/<slug:parasite_name_slug>/',views.show_parasite, name='show_parasite'),
>>>>>>> Stashed changes
]