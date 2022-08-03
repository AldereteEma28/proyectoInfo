from .settings import *
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.mysql",
        "NAME": 'project',
        'USER': 'root',
        'PASSWORD': '199315Ale',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#Ale
