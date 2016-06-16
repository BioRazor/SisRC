from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'df338krfvhjohs',
        'USER': 'iavsvfdwxhooez',
        'PASSWORD': 'guO0pvXH80K8f_hy5Pito2eKJZ',
        'HOST': 'ec2-54-221-235-135.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR.child('static'),)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')