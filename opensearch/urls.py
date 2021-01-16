# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/urls.py


from typing import List, Union  # pylint: disable=W0611

from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver  # pylint: disable=W0611

from opensearch.views import opensearch


__all__ = ["urlpatterns"]  # type: List[str]


# opensearch urls
urlpatterns = [
    re_path(r"^opensearch\.xml$", opensearch, name="opensearch")  # opensearch
]  # type: List[Union[URLPattern, URLResolver]]
