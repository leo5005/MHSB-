from .base import *
import os
import environ

ALLOWED_HOSTS = ['*']

DEBUG = True

env = environ.Env()
env.read_env('.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'