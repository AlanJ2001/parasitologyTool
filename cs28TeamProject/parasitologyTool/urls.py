from django.conf.urls import url
from parasitologyTool import views
from django.urls import path

app_name = 'parasitologyTool'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #path('add_post/', views.add_post, name='add_post'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('public_content/', views.public_content, name='public_content'),
    path('public_content/<int:parasite_id>/add_article/',views.add_article, name='add_article'),
    path('public_content/<int:parasite_id>/', views.public_parasite_page, name = 'public_parasite_page'),
    path('public_content/add_parasite/', views.add_parasite, name='add_parasite'),
    path('public_content/goto/', views.goto_parasite, name='goto'),
    path('clinical_portal/', views.clinical_portal, name = 'clinical_portal'),
    path('clinical_portal/<int:parasite_id>/', views.clinical_parasite_page, name = 'clinical_parasite_page'),
    path('clinical_portal/<int:parasite_id>/add_post/',views.add_post, name='add_post'),
    path('research_portal/', views.research_portal, name = 'research_portal'),
    path('research_portal/<int:parasite_id>/', views.research_parasite_page, name = 'research_parasite_page'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('research_portal/<int:parasite_id>/add_post/',views.add_research_post, name='add_research_post'),
    path('research_portal/<int:parasite_id>/<int:post_id>',views.research_post_page, name='research_post_page'),
]