from .base import *
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://blog-uocra-grupo6.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dt6pjc5j5ij3f',
        'USER': 'lexswfjynwsdvv',
        'PASSWORD': '34ff2e5663dfded280091e459d2b1b58aa7cbffa9870a56e88faa0c14f1f63b0',
        'HOST': 'ec2-52-200-5-135.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}