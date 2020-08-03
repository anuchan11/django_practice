import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
import django
django.setup()

from faker import Faker
from myApp.models import Users

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        name = fakegen.name().split()
        fake_fname = name[0]
        fake_lname = name[1]
        fake_email = fakegen.email()
        u = Users.objects.get_or_create(fname=fake_fname, lname=fake_lname, email=fake_email)[0]


if __name__ == "__main__":
    print("Populating data.....")
    populate(20)
    print("DONE")
