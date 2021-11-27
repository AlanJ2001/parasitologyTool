import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs28TeamProject.settings')

import django
django.setup()
from parasitologyTool.models import Parasite, Article

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/'} ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask',
         'url':'http://flask.pocoo.org'} ]

    parasites = {'Python': {'article': python_pages},
            'Other Frameworks': {'article': other_pages} }

    for para, para_data in parasites.items():
        c = add_parasite(para)
        for a in para_data['article']:
            add_article(c, a['title'], a['url'])

    for c in Parasite.objects.all():
        for a in Article.objects.filter(parasite=c):
            print(f'- {c}: {a}')



def add_parasite(name):
    c = Parasite.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_article(parasite, title, url, views=0):
    a = Article.objects.get_or_create(parasite=parasite, title=title)[0]
    a.url =url
    a.views = views
    a.save()
    return a

if __name__ == '__main__':
    print("populating...")
    populate()