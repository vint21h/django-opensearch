# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/conf.py


from typing import List  # pylint: disable=W0611

from appconf import AppConf
from django.conf import settings


__all__ = ["settings"]  # type: List[str]


class DjangoOpensearchAppConf(AppConf):
    """
    Django opensearch.xml settings.
    """

    CONTACT_EMAIL = getattr(settings, "OPENSEARCH_CONTACT_EMAIL", "")  # type: str
    SHORT_NAME = getattr(settings, "OPENSEARCH_SHORT_NAME", "")  # type: str
    DESCRIPTION = getattr(settings, "OPENSEARCH_DESCRIPTION", "")  # type: str
    FAVICON_WIDTH = getattr(settings, "OPENSEARCH_FAVICON_WIDTH", 16)  # type: int
    FAVICON_HEIGHT = getattr(settings, "OPENSEARCH_FAVICON_HEIGHT", 16)  # type: int
    FAVICON_TYPE = getattr(
        settings, "OPENSEARCH_FAVICON_TYPE", "image/x-icon"
    )  # type: str
    FAVICON_FILE = getattr(
        settings, "OPENSEARCH_FAVICON_FILE", "favicon.ico"
    )  # type: str
    SEARCH_URL = getattr(settings, "OPENSEARCH_SEARCH_URL", "search")  # type: str
    SEARCH_QUERYSTRING = getattr(
        settings, "OPENSEARCH_SEARCH_QUERYSTRING", "q="
    )  # type: str
    INPUT_ENCODING = getattr(
        settings, "OPENSEARCH_INPUT_ENCODING", "UTF-8"
    )  # type: str

    class Meta:
        """
        Config settings.
        """

        prefix = "opensearch"  # type: str
