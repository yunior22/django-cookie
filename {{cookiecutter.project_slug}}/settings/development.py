from config.settings import *  # noqa
from config.settings import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('APP_DEBUG', True)
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('APP_SECRET_KEY')
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('APP_ALLOWED_HOST')


# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    }
}


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
if env('DB_ENGINE') == 'psql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': env('DB_HOST'),
            'NAME': env('DB_DATABASE'),
            'USER': env('DB_USERNAME'),
            'PASSWORD': env('DB_PASSWORD'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ROOT_DIR / 'db_database.sqlite3',
        }
    }


# Your dev settings...
# ------------------------------------------------------------------------------
