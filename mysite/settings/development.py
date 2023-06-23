from .base import *
import os

ALLOWED_HOSTS = ['*']

DEBUG = True

SECRET_KEY = 'd7s4=xvh@p7lksbs5ag#(!fh6@pwy23zh6a&i@wp3g)((%%iue'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'