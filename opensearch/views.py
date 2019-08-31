# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/views.py


from typing import Dict, List, Union  # pylint: disable=W0611

from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render_to_response
from django.urls import reverse

from opensearch.conf import settings


__all__ = ["opensearch"]  # type: List[str]


def opensearch(request: HttpRequest) -> HttpResponse:
    """
    Render opensearch.xml.

    :param request: django request instance.
    :type request: django.http.request.HttpRequest.
    :return: rendered opensearch.xml
    :rtype: django.http.HttpResponse.
    """

    context = {
        "OPENSEARCH_CONTACT_EMAIL": settings.OPENSEARCH_CONTACT_EMAIL,
        "OPENSEARCH_SHORT_NAME": settings.OPENSEARCH_SHORT_NAME,
        "OPENSEARCH_DESCRIPTION": settings.OPENSEARCH_DESCRIPTION,
        "OPENSEARCH_FAVICON_WIDTH": settings.OPENSEARCH_FAVICON_WIDTH,
        "OPENSEARCH_FAVICON_HEIGHT": settings.OPENSEARCH_FAVICON_HEIGHT,
        "OPENSEARCH_FAVICON_TYPE": settings.OPENSEARCH_FAVICON_TYPE,
        "OPENSEARCH_FAVICON_FILE": settings.OPENSEARCH_FAVICON_FILE,
        "OPENSEARCH_URL": "{url}?{querystring}{{searchTerms}}".format(
            **{
                "url": request.build_absolute_uri(
                    reverse(settings.OPENSEARCH_SEARCH_URL)
                ),
                "querystring": settings.OPENSEARCH_SEARCH_QUERYSTRING,
            }
        ),
        "OPENSEARCH_INPUT_ENCODING": settings.OPENSEARCH_INPUT_ENCODING.upper(),
    }  # type: Dict[str, Union[str, int]]

    return render_to_response(
        "opensearch/opensearch.xml",
        context=context,
        content_type="application/opensearchdescription+xml",
    )
