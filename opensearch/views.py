# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/views.py


from typing import Dict, List, Union

from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render, resolve_url

from opensearch.conf import settings


__all__: List[str] = ["opensearch"]


def opensearch(request: HttpRequest) -> HttpResponse:
    """
    Render opensearch.xml.

    :param request: django request instance
    :type request: HttpRequest
    :return: rendered opensearch.xml
    :rtype: HttpResponse
    """
    context: Dict[str, Union[str, int]] = {
        "OPENSEARCH_CONTACT_EMAIL": settings.OPENSEARCH_CONTACT_EMAIL,
        "OPENSEARCH_SHORT_NAME": settings.OPENSEARCH_SHORT_NAME,
        "OPENSEARCH_DESCRIPTION": settings.OPENSEARCH_DESCRIPTION,
        "OPENSEARCH_FAVICON_WIDTH": settings.OPENSEARCH_FAVICON_WIDTH,
        "OPENSEARCH_FAVICON_HEIGHT": settings.OPENSEARCH_FAVICON_HEIGHT,
        "OPENSEARCH_FAVICON_TYPE": settings.OPENSEARCH_FAVICON_TYPE,
        "OPENSEARCH_FAVICON_FILE": settings.OPENSEARCH_FAVICON_FILE,
        "OPENSEARCH_URL": "{url}?{querystring}{{searchTerms}}".format(  # noqa: FS002
            **{
                "url": request.build_absolute_uri(
                    resolve_url(to=settings.OPENSEARCH_SEARCH_URL)
                ),
                "querystring": settings.OPENSEARCH_SEARCH_QUERYSTRING,
            }
        ),
        "OPENSEARCH_INPUT_ENCODING": settings.OPENSEARCH_INPUT_ENCODING.upper(),
        "OPENSEARCH_URL_SUGGEST": "{url}?{querystring}{{searchTerms}}".format(
            **{
                "url": request.build_absolute_uri(
                    resolve_url(to=settings.OPENSEARCH_SEARCH_URL_SUGGEST)
                ),
                "querystring": settings.OPENSEARCH_SEARCH_QUERYSTRING_SUGGEST,
            }
        ),
        "OPENSEARCH_MOZ_FORM": settings.OPENSEARCH_MOZ_FORM,
    }

    return render(
        request=request,
        template_name="opensearch/opensearch.xml",
        context=context,
        content_type="application/opensearchdescription+xml",
    )
