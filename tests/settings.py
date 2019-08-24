# -*- coding: utf-8 -*-

# django-opensearch
# settings/settings.py


import pathlib
import sys


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY = "django-opensearch-test-key"  # type: str

# configure databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "django-opensearch-tests.sqlite3",
    }
}  # type: dict

# configure templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]  # type: list


# add nose test runner application and django-opensearch
INSTALLED_APPS = ["django_nose", "opensearch"]  # type: list

# add nose test runner
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"  # type: str

# configure nose test runner
NOSE_ARGS = [
    "--rednose",
    "--force-color",
    "--with-timer",
    "--with-doctest",
    "--with-coverage",
    "--cover-inclusive",
    "--cover-erase",
    "--cover-package=opensearch",
    "--logging-clear-handlers",
]  # type: list

# configure urls
ROOT_URLCONF = "opensearch.urls"  # type: str
