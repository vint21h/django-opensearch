# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/settings.py


from __future__ import unicode_literals

from django.conf import settings


__all__ = [
    "CONTACT_EMAIL",
    "SHORT_NAME",
    "DESCRIPTION",
    "FAVICON_WIDTH",
    "FAVICON_HEIGHT",
    "FAVICON_TYPE",
    "FAVICON_FILE",
    "SEARCH_URL",
    "SEARCH_QUERYSTRING",
    "INPUT_ENCODING",
]


CONTACT_EMAIL = getattr(settings, "OPENSEARCH_CONTACT_EMAIL", "")
SHORT_NAME = getattr(settings, "OPENSEARCH_SHORT_NAME", "")
DESCRIPTION = getattr(settings, "OPENSEARCH_DESCRIPTION", "")
FAVICON_WIDTH = getattr(settings, "OPENSEARCH_FAVICON_WIDTH", 16)
FAVICON_HEIGHT = getattr(settings, "OPENSEARCH_FAVICON_HEIGHT", 16)
FAVICON_TYPE = getattr(settings, "OPENSEARCH_FAVICON_TYPE", "image/x-icon")
FAVICON_FILE = getattr(settings, "OPENSEARCH_FAVICON_FILE", "favicon.ico")
SEARCH_URL = getattr(settings, "OPENSEARCH_SEARCH_URL", "search")
SEARCH_QUERYSTRING = getattr(settings, "OPENSEARCH_SEARCH_QUERYSTRING", "q=")
INPUT_ENCODING = getattr(settings, "OPENSEARCH_INPUT_ENCODING", "UTF-8")
