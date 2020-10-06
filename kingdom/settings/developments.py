from .base import *

ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret("DB_SCHEMA"),
        'USER': get_secret("DB_USER"),
        'PASSWORD': get_secret("DB_PASSWORD"),
        'HOST': get_secret("DB_HOST"),
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8'}
    }
}