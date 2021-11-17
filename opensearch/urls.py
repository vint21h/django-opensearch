# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/urls.py


from typing import List, Union

from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver

from opensearch.views import opensearch


__all__: List[str] = ["urlpatterns"]


# opensearch urls
urlpatterns: List[Union[URLPattern, URLResolver]] = [
    re_path(r"^opensearch\.xml$", opensearch, name="opensearch")  # opensearch
]
