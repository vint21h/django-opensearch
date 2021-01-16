# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/apps.py


from typing import List  # pylint: disable=W0611

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__ = ["DjangoOpensearchConfig"]  # type: List[str]


class DjangoOpensearchConfig(AppConfig):
    """
    Django opensearch.xml config.
    """

    name = "opensearch"  # type: str
    verbose_name = _("Django opensearch.xml")  # type: str
