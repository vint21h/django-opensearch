# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/urls.py

from __future__ import unicode_literals

from django.conf.urls import url
from opensearch.views import opensearch

# opensearch urls

urlpatterns = [
    url(r"^opensearch\.xml$", opensearch, name="opensearch"),  # opensearch
]
