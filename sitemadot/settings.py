import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-po44qz%wmh++fctxeq6&xik%@adifzo8%6@dt4b@xxyv85z6yu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'madot',
]

JAZZMIN_SETTINGS = {
    # Nom et sous-titre
    "site_title": "MADAGASTOURS Admin",
    "site_header": "Admin MADAGASTOURS",
    "welcome_sign": "Bienvenue sur l'administration de MADAGASTOURS",

    # Personnalisation du menu
    "custom_links": {
        "app_label": [{
            "name": "Statistiques",
            "url": "custom-stats-view",
            "icon": "fas fa-chart-line",
        }],
    },

    # Icônes pour les modèles
    "icons": {
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "madot.Destination": "fas fa-plane",
    },

    # Interface utilisateur
    "show_version": False,  # Masquer la version de Jazzmin
    "ui_darkmode": True,  # Utiliser le mode sombre
    "show_sidebar_menu": True,  # Afficher le menu latéral
    "menu_icon_classes": "fas fa-bars",  # Icône du menu
    "show_submenu_icons": True,  # Afficher les icônes des sous-menus
    "hide_sidebar_menu_items": [],  # Masquer des éléments du menu latéral
    "hide_sidebar_menu_icons": [],  # Masquer des icônes du menu latéral
    "show_footer": True,  # Afficher le pied de page
    "default_menu_item": "home",  # Élément de menu par défaut
    "navigation_expanded": True,  # Toujours afficher le menu complet
    "order_with_respect_to": ["auth", "madot"],  # Ordre des applications
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sitemadot.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'sitemadot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.madagastours.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fenitria@madagastours.com'
EMAIL_HOST_PASSWORD = 'Jose21v07e02'
DEFAULT_FROM_EMAIL = 'fenitria@madagastours.com'

import ssl
from django.core.mail import get_connection

# Désactive la vérification SSL
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None

# Ignore SSL Verification
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
connection = get_connection()
connection.use_tls = False
connection.use_ssl = False
connection.ssl_context = ssl._create_unverified_context()

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
