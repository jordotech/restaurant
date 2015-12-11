from .base import *
import os
DEBUG = True
SITE_ID = 2
def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'settings.jordan.show_toolbar',
}

INSTALLED_APPS += (
    'debug_toolbar',
    'template_debug',
)


SECRET_KEY = os.environ["SECRET_KEY_LOCAL"]
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'restaurant',
        #'USER': 'postgres',
        'USER': 'root',
        #'PASSWORD': 'Login4040',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {'init_command':'SET NAMES "utf8"'}
    },
}