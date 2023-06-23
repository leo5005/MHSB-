from .base import *
import environ
import os

DEBUG = False

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

ALLOWED_HOSTS = ['mhsb-kt.herokuapp.com',]

DATABASES = {
    'default': env.db(),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': env('CLOUDINARY_API_KEY'),
    'API_SECRET': env('CLOUDINARY_API_SECRET'),
}
