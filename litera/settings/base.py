"""
Django settings for litera project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get("DEBUG", "").lower() == "false" else True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*", ]

ADMINS = (
    # ("name", "email"),
)
MANAGERS = ADMINS


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'de'
USE_I18N = True
USE_L10N = True

TIME_ZONE = 'UTC'
USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'
MEDIA_URL_PREFIX = ''


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'columns.context_processors.media_urls',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'south',

    'mptt',
    'feincms',
    'feincms.module.page',
    'feincms.module.medialibrary',

    'elephantblog',
    'form_designer',

    'columns',
    'debug_toolbar',
)


ROOT_URLCONF = 'litera.urls'

WSGI_APPLICATION = 'litera.wsgi.application'

EMAIL_SUBJECT_PREFIX = '[litera] '

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')  # FIXME

# django-compressor settings
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# Auth settings
LOGIN_URL = 'django.contrib.auth.views.login'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'litera.db'),
    }
}


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SOUTH_MIGRATION_MODULES = {
    'page': 'columns.fein_migrations.page',
    'medialibrary': 'columns.fein_migrations.medialibrary',
    'elephantblog': 'columns.fein_migrations.elephantblog',
    'form_designer': 'columns.fein_migrations.form_designer',
}

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "ACSAFasdfasdEEEEEFasdFsdFas.s-.,344SDFAdfa{ew''sfq3352425t5!+%.-,4r324fASDVDFVre"
)

FEINCMS_USE_PAGE_ADMIN = False

FEINCMS_RICHTEXT_INIT_TEMPLATE = 'admin/content/richtext/init_ckeditor_litera.html'
FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'CKEDITOR_JS_URL': os.path.join(STATIC_URL, 'js/ckeditor/ckeditor.js'),
    'CKEDITOR_JS_CONFIG_URL': os.path.join(STATIC_URL, 'js/ckeditor/config.js'),
}


def elephantblog_entry_url_app(self):
    from feincms.content.application.models import app_reverse
    return app_reverse('elephantblog_entry_detail', 'elephantblog.urls', kwargs={
        'year': self.published_on.strftime('%Y'),
        'month': self.published_on.strftime('%m'),
        'day': self.published_on.strftime('%d'),
        'slug': self.slug,
        })


def elephantblog_categorytranslation_url_app(self):
    from feincms.content.application.models import app_reverse
    return app_reverse(
        'elephantblog_category_detail', 'elephantblog.urls',
        kwargs={'slug': self.slug, }
    )


ABSOLUTE_URL_OVERRIDES = {
    'elephantblog.entry': elephantblog_entry_url_app,
    'elephantblog.categorytranslation': elephantblog_categorytranslation_url_app,
}

BLOG_PAGINATE_BY = 10

DEBUG_TOOLBAR_PATCH_SETTINGS = False
