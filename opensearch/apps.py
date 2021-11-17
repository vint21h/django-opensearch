# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/apps.py


from typing import List

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["DjangoOpensearchConfig"]


class DjangoOpensearchConfig(AppConfig):
    """Django opensearch.xml config."""

    name: str = "opensearch"
    verbose_name: str = _("Django opensearch.xml")
