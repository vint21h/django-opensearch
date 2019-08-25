# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/apps.py


from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


__all__ = ["DjangoOpensearchConfig"]  # type: list


class DjangoOpensearchConfig(AppConfig):

    name = "opensearch"
    verbose_name = _("Django opensearch.xml")
