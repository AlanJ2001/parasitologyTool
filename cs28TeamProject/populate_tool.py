import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs28TeamProject.settings')

import django

django.setup()
from parasitologyTool.models import Parasite


def populate():
    parasites = ['Trypanosoma', 'Plasmodium', 'Leishmania', 'Toxoplasma', 'Helminths']
    for p in parasites:
        c = add_parasite(p)


def add_parasite(p):
    c = Parasite.objects.get_or_create(name=p)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("populating...")
    populate()
