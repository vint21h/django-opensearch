# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/conf.py


from typing import List

from appconf import AppConf
from django.conf import settings


__all__: List[str] = ["settings"]


class DjangoOpensearchAppConf(AppConf):
    """Django opensearch.xml settings."""

    CONTACT_EMAIL: str = getattr(settings, "OPENSEARCH_CONTACT_EMAIL", "")
    SHORT_NAME: str = getattr(settings, "OPENSEARCH_SHORT_NAME", "")
    DESCRIPTION: str = getattr(settings, "OPENSEARCH_DESCRIPTION", "")
    FAVICON_WIDTH: int = getattr(settings, "OPENSEARCH_FAVICON_WIDTH", 16)
    FAVICON_HEIGHT: int = getattr(settings, "OPENSEARCH_FAVICON_HEIGHT", 16)
    FAVICON_TYPE: str = getattr(settings, "OPENSEARCH_FAVICON_TYPE", "image/x-icon")
    FAVICON_FILE: str = getattr(settings, "OPENSEARCH_FAVICON_FILE", "favicon.ico")
    SEARCH_URL: str = getattr(settings, "OPENSEARCH_SEARCH_URL", "search")
    SEARCH_QUERYSTRING: str = getattr(settings, "OPENSEARCH_SEARCH_QUERYSTRING", "q=")
    INPUT_ENCODING: str = getattr(settings, "OPENSEARCH_INPUT_ENCODING", "UTF-8")

    class Meta:
        """Config settings."""

        prefix: str = "opensearch"
