from .base import *
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.mysql",
        "NAME": 'proyecto',
        'USER': 'root',
        'PASSWORD': 'usuarioroot',
        'HOST': 'localhost',
        'PORT': '',
    }
}

