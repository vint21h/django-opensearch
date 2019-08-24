# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/apps.py


from django.apps import AppConfig


__all__ = ["DjangoOpensearchConfig"]  # type: list


class DjangoOpensearchConfig(AppConfig):

    name = "opensearch"
    verbose_name = "Django opensearch.xml"
