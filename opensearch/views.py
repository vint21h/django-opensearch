# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/views.py


from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render_to_response
from django.urls import reverse

from opensearch import settings


__all__ = ["opensearch"]


def opensearch(request: HttpRequest) -> HttpResponse:
    """
    Return opensearch.xml.

    :param request: django request instance.
    :type request: django.http.request.HttpRequest.
    :return: rendered opensearch.xml
    :rtype: django.http.HttpResponse.
    """

    contact_email = settings.CONTACT_EMAIL
    short_name = settings.SHORT_NAME
    description = settings.DESCRIPTION
    favicon_width = settings.FAVICON_WIDTH
    favicon_height = settings.FAVICON_HEIGHT
    favicon_type = settings.FAVICON_TYPE
    favicon_file = settings.FAVICON_FILE
    url = "{url}?{querystring}{{searchTerms}}".format(
        **{
            "url": request.build_absolute_uri(reverse(settings.SEARCH_URL)),
            "querystring": settings.SEARCH_QUERYSTRING,
        }
    )
    input_encoding = settings.INPUT_ENCODING.upper()

    return render_to_response(
        "opensearch/opensearch.xml",
        context=locals(),
        content_type="application/opensearchdescription+xml",
    )
