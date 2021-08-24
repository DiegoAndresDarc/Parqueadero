import os
from base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'parking_lot',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

MEDIA_URL = '/docs/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)
