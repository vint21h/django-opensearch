# -*- coding: utf-8 -*-

# django-opensearch
# tests/settings.py


import sys
import pathlib
from random import SystemRandom
from typing import Dict, List, Union


# black magic to use imports from library code
path = pathlib.Path(__file__).absolute()
project = path.parent.parent.parent
sys.path.insert(0, str(project))

# secret key
SECRET_KEY: str = "".join(
    [
        SystemRandom().choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")
        for i in range(50)
    ]
)

# security settings
ALLOWED_HOSTS: List[str] = ["example.com"]

# configure databases
DATABASES: Dict[str, Dict[str, str]] = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

# configure templates
TEMPLATES: List[Dict[str, Union[str, List[str], bool, Dict[str, str]]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]


INSTALLED_APPS: List[str] = ["opensearch"]

# configure urls
ROOT_URLCONF: str = "opensearch.urls"

# opensearch settings
OPENSEARCH_CONTACT_EMAIL: str = "test@example.com"
OPENSEARCH_SHORT_NAME: str = "opensearch"
OPENSEARCH_DESCRIPTION: str = "Search engine human-readable text description"
OPENSEARCH_FAVICON_WIDTH: int = 16
OPENSEARCH_FAVICON_HEIGHT: int = 16
OPENSEARCH_FAVICON_TYPE: str = "image/x-icon"
OPENSEARCH_FAVICON_FILE: str = "favicon.ico"
OPENSEARCH_SEARCH_URL: str = "search"
OPENSEARCH_SEARCH_QUERYSTRING: str = "q="
OPENSEARCH_INPUT_ENCODING: str = "UTF-8"
