# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/urls.py


from django.conf.urls import url

from opensearch.views import opensearch


__all__ = ["urlpatterns"]  # type: list


# opensearch urls
urlpatterns = [
    url(r"^opensearch\.xml$", opensearch, name="opensearch")  # opensearch
]  # type: list
