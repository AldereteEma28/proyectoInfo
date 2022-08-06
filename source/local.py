from .settings import *
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.mysql",
        "NAME": 'project',
        'USER': 'root',
        'PASSWORD': 'insadanibra@123Q',
        'HOST': 'localhost',
        'PORT': '',
    }
}

