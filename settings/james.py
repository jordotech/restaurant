from .base import *
import os
DEBUG = True
SITE_ID = 2
def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'settings.james.show_toolbar',
}

INSTALLED_APPS += (
    'debug_toolbar',
    'template_debug',
)


SECRET_KEY = os.environ["SECRET_KEY_LOCAL"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'restaurant',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword goes here',
        'HOST': '',
        'PORT': '',
    },
}