# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/urls.py

from django.conf.urls import patterns, url

# opesearch urls
urlpatterns = patterns('opensearch.views',
    url(r'^opensearch\.xml$', 'opensearch', name="opensearch"),  # opensearch
)
