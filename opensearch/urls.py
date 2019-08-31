# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/urls.py


from typing import List, Union  # noqa: W0611

from django.conf.urls import url
from django.urls.resolvers import URLPattern, URLResolver

from opensearch.views import opensearch


__all__ = ["urlpatterns"]  # type: List[str]


# opensearch urls
urlpatterns = [
    url(r"^opensearch\.xml$", opensearch, name="opensearch")  # opensearch
]  # type: List[Union[URLPattern, URLResolver]]
