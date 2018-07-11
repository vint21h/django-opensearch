# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/templatetags/opensearch_tags.py


from __future__ import unicode_literals

from django import template

from opensearch import settings


__all__ = [
    "opensearch_meta",
]


register = template.Library()


@register.inclusion_tag("opensearch/templatetags/opensearch_meta.html", takes_context=True)
def opensearch_meta(context):
    """
    Return meta rel opensearch tag.
    """

    context.update({
        "DESCRIPTION": settings.DESCRIPTION,
    })

    return context
