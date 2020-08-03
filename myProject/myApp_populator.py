import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
import django
django.setup()

import random

from myApp.models import AccessRecord, WebPage, Topic

from faker import Faker

fakegen = Faker()

topics = ["Social", "Game", "News", "Sports","Knowledge"]

def add_topic():
    t = Topic.objects.get_or_create(top_name= random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_name = fakegen.name()
        fake_date = fakegen.date()
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        accrec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == "__main__":
    print("Populating the data......")
    populate(17)
    print("DONE!!")
