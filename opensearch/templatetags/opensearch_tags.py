# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/templatetags/opensearch_tags.py


from typing import Dict, List  # pylint: disable=W0611

from django import template

from opensearch.conf import settings


__all__ = ["opensearch_meta"]  # type: List[str]


register = template.Library()


@register.inclusion_tag("opensearch/templatetags/opensearch_meta.html")
def opensearch_meta() -> Dict[str, str]:
    """
    Return meta rel opensearch tag.

    :return: opensearch description
    :rtype: Dict[str, str]
    """

    return {"OPENSEARCH_DESCRIPTION": settings.OPENSEARCH_DESCRIPTION}
