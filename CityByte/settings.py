import os
import environ
from pathlib import Path

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-cm&ek+rlsg%=@47_^f7@^_d0o6^#azfb%oel1h8x65c06*b2u8"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'https://localhost:8000']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "corsheaders",
    "search",
    "info",
    "CityByte",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "CityByte.urls"

CORS_ALLOW_ALL_ORIGINS = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "CityByte.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static", ]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "TIMEOUT": 3600,
    }
}

GEODB_CONFIG = {
    "protocol": "https",
    "host": "wft-geo-db.p.rapidapi.com",
    "port": 443,
    "headers": {
        "x-rapidapi-key": env("GEODB_X_RAPID_API_KEY"),
        "x-rapidapi-host": env("GEODB_X_RAPID_API_HOST"),
    },
}

AMADEUS_CONFIG = {
    "protocol": "https",
    "host": "test.api.amadeus.com",
    "port": 443,
    "headers": {
        "API_KEY": env("AMADEUS_API_KEY"),
        "API_SECRET_KEY": env("AMADEUS_API_SECRET_KEY"),
    },
}

UNSPLASH_CONFIG = {
    "protocol": "https",
    "host": "api.unsplash.com",
    "port": 443,
    "headers": {
        "Authorization": f"Client-ID {env('UNSPLASH_API_KEY')}",
    },
}

FOURSQUARE_CONFIG = {
    "protocol": "https",
    "host": "api.foursquare.com",
    "port": 443,
    "headers": {
        "Authorization": env("FOURSQUARE_API_KEY"),
    },
}

WEATHER_BIT_CONFIG = {
    "base_url": "https://api.weatherbit.io/v2.0/current",
    "api_key": env("WEATHER_BIT_X_RAPID_API_KEY"),
}



# Email Backend Configuration for sending password reset emails
LOGIN_REDIRECT_URL = "main_page"
LOGOUT_REDIRECT_URL = "login"
#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
CRISPY_TEMPLATE_PACK = "bootstrap"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'nirmit.pce20@sot.pdpu.ac.in'


NEWSAPI_CONFIG = {
    "base_url": "https://newsapi.org/v2",
    "api_key": env("NEWSAPI_KEY"),
}



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nirmit.pce20@sot.pdpu.ac.in'
EMAIL_HOST_PASSWORD = 'abjdkmuqcqkcwaqw'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

