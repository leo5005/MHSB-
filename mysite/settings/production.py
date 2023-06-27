from .base import *
import environ
import os
import psycopg2
import dj_database_url

DEBUG = False

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

#ALLOWED_HOSTS = ['mhsb-kt.herokuapp.com']
ALLOWED_HOSTS = ['*']

#DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

DATABASES = {
    'default': env.db(),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': env('CLOUDINARY_API_KEY'),
    'API_SECRET': env('CLOUDINARY_API_SECRET'),
}


DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}