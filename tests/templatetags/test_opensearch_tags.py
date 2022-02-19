# -*- coding: utf-8 -*-

# django-opensearch
# tests/templatetags/test_opensearch_tags.py


from typing import Dict, List

from django.test import TestCase
from django.template import Context, Template
from django.test.utils import override_settings

from opensearch.conf import settings
from opensearch.templatetags.opensearch_tags import opensearch_meta


__all__: List[str] = ["OpensearchMetaTemplatetagTest"]


class OpensearchMetaTemplatetagTest(TestCase):
    """Opensearch meta templatetag tests."""

    def test_opensearch_meta__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, str] = opensearch_meta()
        expected: Dict[str, str] = {
            "OPENSEARCH_DESCRIPTION": settings.OPENSEARCH_DESCRIPTION
        }

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_opensearch_meta__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load opensearch_tags %}
            {% opensearch_meta %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = '<link rel="search" type="application/opensearchdescription+xml" title="Search engine human-readable text description" href="/opensearch.xml" />'  # noqa: E501

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(OPENSEARCH_DESCRIPTION="")
    def test_opensearch_meta__render__without_description(self) -> None:
        """Test templatetag rendering result without description."""
        template: Template = Template(
            """
            {% load opensearch_tags %}
            {% opensearch_meta %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)
