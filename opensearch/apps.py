# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/apps.py

from __future__ import unicode_literals

from django.apps import AppConfig

__all__ = ["OpensearchConfig", ]


class OpensearchConfig(AppConfig):

    name = "opensearch"
    verbose_name = "Django opensearch"