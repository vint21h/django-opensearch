# -*- coding: utf-8 -*-

# django-opensearch
# tests/settings.py


import pathlib
import sys


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY = "django-opensearch-test-key"  # type: str

# security settings
ALLOWED_HOSTS = ["example.com"]

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

# opensearch settings
OPENSEARCH_CONTACT_EMAIL = "test@example.com"  # type: str
OPENSEARCH_SHORT_NAME = "opensearch"  # type: str
OPENSEARCH_DESCRIPTION = "Search engine human-readable text description"  # type: str
OPENSEARCH_FAVICON_WIDTH = 16  # type: int
OPENSEARCH_FAVICON_HEIGHT = 16  # type: int
OPENSEARCH_FAVICON_TYPE = "image/x-icon"  # type str
OPENSEARCH_FAVICON_FILE = "favicon.ico"  # type: str
OPENSEARCH_SEARCH_URL = "search"  # type: str
OPENSEARCH_SEARCH_QUERYSTRING = "q="  # type: str
OPENSEARCH_INPUT_ENCODING = "UTF-8"  # type: str
