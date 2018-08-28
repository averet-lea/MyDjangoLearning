import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import AccessRecord,Topic,Webpage,user
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        webp = Webpage.objects.get_or_create(topic=top,url=fake_name,name=fake_name)[0]
        accr = AccessRecord.objects.get_or_create(name=webp,date=fake_date)[0]

def populateUsers(N=5):
    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()
        users = user.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)[0]

if __name__ == '__main__':
    print("Population data...")
    Topic.objects.all().delete()
    Webpage.objects.all().delete()
    AccessRecord.objects.all().delete()
    user.objects.all().delete()
#    populate(20)
#    populateUsers(30)
    print('Complete')
