from .base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'
