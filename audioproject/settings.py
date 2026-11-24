
from pathlib import Path
import environ

# ==================================================
# BASE DIRECTORY
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==================================================
# ENVIRONMENT VARIABLES
# ==================================================

env = environ.Env()

environ.Env.read_env(BASE_DIR / ".env")

# ==================================================
# SECURITY SETTINGS
# ==================================================

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=[
        "localhost",
        "127.0.0.1",
        ".onrender.com",
    ],
)

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=[
        "https://*.onrender.com",
    ],
)

# ==================================================
# ASSEMBLYAI API CONFIGURATION
# ==================================================

API_KEY_ASSEMBLYAI = env(
    "API_KEY_ASSEMBLYAI",
    default="",
)

# ==================================================
# INSTALLED APPLICATIONS
# ==================================================

INSTALLED_APPS = [
    # Custom application
    "audioapp.apps.AudioappConfig",

    # Django built-in applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==================================================
# URL CONFIGURATION
# ==================================================

ROOT_URLCONF = "audioproject.urls"

# ==================================================
# TEMPLATE CONFIGURATION
# ==================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# ==================================================
# WSGI APPLICATION
# ==================================================

WSGI_APPLICATION = "audioproject.wsgi.application"

# ==================================================
# DATABASE CONFIGURATION
# ==================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ==================================================
# PASSWORD VALIDATION
# ==================================================

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

# ==================================================
# LANGUAGE AND TIME
# ==================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# ==================================================
# STATIC FILE CONFIGURATION
# ==================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_DIRECTORY = BASE_DIR / "static"

STATICFILES_DIRS = (
    [STATIC_DIRECTORY]
    if STATIC_DIRECTORY.exists()
    else []
)

# ==================================================
# MEDIA FILE CONFIGURATION
# ==================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# ==================================================
# WHITENOISE CONFIGURATION
# ==================================================

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# ==================================================
# DEFAULT PRIMARY KEY
# ==================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==================================================
# DJANGO ERROR LOGGING
# ==================================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {name} {message}",
            "style": "{",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },

    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },

        "django": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
    },

    "root": {
        "handlers": ["console"],
        "level": "ERROR",
    },
}
