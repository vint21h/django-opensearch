# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/views.py


from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from opensearch import settings


__all__ = [
    "opensearch",
]


def opensearch(request):
    """
    Return opensearch.xml.
    """

    contact_email = settings.CONTACT_EMAIL
    short_name = settings.SHORT_NAME
    description = settings.DESCRIPTION
    favicon_width = settings.FAVICON_WIDTH
    favicon_height = settings.FAVICON_HEIGHT
    favicon_type = settings.FAVICON_TYPE
    favicon_file = settings.FAVICON_FILE
    url = "{url}?{querystring}{{searchTerms}}".format(**{
        "url": request.build_absolute_uri(reverse(settings.SEARCH_URL)),
        "querystring": settings.SEARCH_QUERYSTRING,
    })
    input_encoding = settings.INPUT_ENCODING.upper()

    return render_to_response("opensearch/opensearch.xml", context=locals(), content_type="application/opensearchdescription+xml")
