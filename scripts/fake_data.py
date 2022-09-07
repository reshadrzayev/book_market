import os
import random

#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_market.settings.")
import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker


def set_user():
    fake = Faker(['en_US'])
    firstName = fake.first_name()
    lastName = fake.last_name()
    userName = f'{firstName}_{lastName}'
    email = f'{userName}@{fake.domain_name()}'

    user_check = User.objects.filter(username=userName)

    while user_check.exists():
        userName = userName + str(random.randrange(1,99))
        user_check = User.objects.filter(username=userName)

    user = User(
        username = userName,
        first_name = firstName,
        last_name = lastName,
        email = email
    )

    user.set_password('testing123')
    user.save()






