from .base import *
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://blog-uocra-grupo6.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dhndv1itek5si',
        'USER': 'irpjycantffodk',
        'PASSWORD': '07be5a56ed656272d020457938f0d65ad6b0b9da57a678b206c9a83ed290f208',
        'HOST': 'ec2-44-209-186-51.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}