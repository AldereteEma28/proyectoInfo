from .base import *
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.mysql",
        "NAME": 'proyecto',
        'USER': 'root',
        'PASSWORD': '199315Ale',
        'HOST': 'localhost',
        'PORT': '',
    }
}

