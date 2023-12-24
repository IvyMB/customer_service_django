import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()
from django.contrib.auth import get_user_model


from core.models import Gender, Country, State
from users.models import CustomUser

User = get_user_model()

def create_country():
    gender = Gender.objects.create(id=1, name='F')
    gender.save()
    country = Country.objects.create(id= 1, name='Brasil', code='BR')
    country.save()

    state = State.objects.create(id=1, name='São Paulo')
    state.save()


def create_super_user():
    user_data = {
        'username': 'ivyM',
        'telephone': '123456789',
        'email': 'vyhofc@gmail.com',
        'gender': Gender.objects.first(),  # Substitua por um objeto Gender existente
        'birthday': '1999-08-17',  # Substitua pela data desejada
        'address': 'Av paulista, 1302',
        'country': Country.objects.first(),  # Substitua por um objeto Country existente
        'state': State.objects.first(),  # Substitua por um objeto State existente
        'hiring_date': '2022-01-01',  # Substitua pela data desejada
        'deactivate_date': None,  # Substitua pela data desejada ou None
    }

    User.objects.create_superuser(**user_data)

if __name__ == "__main__":
    create_country()
    create_super_user()
