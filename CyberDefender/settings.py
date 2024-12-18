"""
Django settings for CyberDefender project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from decouple import config



#Глобальні змінні
NETWORK = None

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m^15e$8j$lw7b5jwqo-skoj-gvp)@zk9yvx)c1)v$1iwf!2t5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['student27.pythonanywhere.com']


#AUTHENTICATION_BACKENDS = (
#    'radiusauth.backends.RADIUSBackend',
#    'django.contrib.auth.backends.ModelBackend',
    #'allauth.account.auth_backends.AuthenticationBackend',
#)

#SITE_ID = 2

#LOGIN_REDIRECT_URL = '/'
#LOGOUT_REDIRECT_URL = '/'
#ACCOUNT_LOGOUT_REDIRECT = '/'


#SOCIALACCOUNT_PROVIDERS = {
#    'google': {
#        'SCOPE' : [
#            'profile',
#            'email'
#        ],
#        'APP': {
#            'client_id':os.getenv("CLIENT_ID"),
#            'secret':os.getenv("CLIENT_SECRET"),
#        },
#        'AUTH_PARAMS': {
#            'access_type':'online',
#        }
#    }
#}

#'client_id': os.environ['CLIENT_ID'],
#'secret': os.environ['CLIENT_SECRET'],

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    #'django_freeradius',
    #'django-radius',
    'django_bootstrap5',
    'CyberDefender',
    'django.contrib.staticfiles',

    #all auth configurations
    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    #'allauth.socialaccount.providers.google'

    # ... include the providers you want to enable:
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.microsoft',
    #'allauth.socialaccount.providers.paypal',
    #'allauth.socialaccount.providers.reddit',
    # 'allauth.socialaccount.providers.telegram',
    #'allauth.socialaccount.providers.twitter',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'CyberDefender.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CyberDefender.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
USE_POSTGRESQL_DB = config("USE_POSTGRESQL_DB", cast=bool)

if USE_POSTGRESQL_DB:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "PORT": config("DB_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_TZ=True


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = '/home/student27/CyberDefender/media'
MEDIA_URL = '/media/'

STATICFILE_LOCATION =  'static'
#STATIC_ROOT = '/home/student27/CyberDefender/static'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

print(BASE_DIR)
print(STATICFILES_DIRS)
#RADIUS_SERVER = '192.168.13.129'
#RADIUS_SECRET = 'your_radius_secret'
