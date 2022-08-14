"""
Django settings for TC_PP_GEN73 project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY", default = 'django-insecure-y&^@va^7bst0-=i9b!n^q96-fst1r*!qflkc$2e+)fi=71x7_=')
# SECRET_KEY = 'django-insecure-y&^@va^7bst0-=i9b!n^q96-fst1r*!qflkc$2e+)fi=71x7_='
# print(SECRET_KEY)
print('Your Secret Key is Protected.')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config("DJANGO_DEBUG", default = True, cast = bool)
DEBUG = True
# print('DEBUG MODE = ', DEBUG, "\n")
# print('Turn Off DEBUG Mode During Deployment.', "\n")

ALLOWED_HOSTS = ['*'] #allow to run on all local machine


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    #3rd party apps
    'crispy_forms',
    'social_django',

    #registering apps
    'accounts.apps.AccountsConfig',
    'blog.apps.BlogConfig',
    'tc_gen.apps.TcGenConfig',
    'pp_gen.apps.PpGenConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TC_PP_GEN73.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'tc_gen.history_context_processor.show_previous_templates',
                'pp_gen.history_context_processor.show_previous_templates',
            ],
        },
    },
]

WSGI_APPLICATION = 'TC_PP_GEN73.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#setting up postgresql database
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'termshub',

        'USER': 'postgres',

        'PASSWORD': '~!@#$%)(*&^hE639',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}


#django-social-auth for db(PostgreSQL)
SOCIAL_AUTH_JSONFIELD_ENABLED = True


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

#social_django custom settings
AUTHENTICATION_BACKENDS = (
    #'social_core.backends.open_id.OpenIdAuth',
    #'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    #'social_core.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "blog/static"),
    # '/var/www/static/',
]

STATIC_URL = 'static/'

#Root directory that serves all static files during production
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')

#for whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/' #root to access the media in the url

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

#redirect to the dashboard page after login
LOGIN_REDIRECT_URL = 'dashboard'

LOGIN_URL = 'signin'

#Email connection settings (for password)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

#accessing environment variables
EMAIL_HOST_USER = config('EMAIL_USER')

EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')

#social authentication ids and passwords
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_SECRET')

SOCIAL_AUTH_FACEBOOK_KEY = config('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('FACEBOOK_SECRET')
