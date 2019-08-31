# -*- coding: utf-8 -*-

# django-opensearch
# tests/templatetags/test_opensearch_tags.py


from typing import Dict, List  # noqa: W0611

from django.template import Context, Template
from django.test import TestCase
from django.test.utils import override_settings

from opensearch.conf import settings
from opensearch.templatetags.opensearch_tags import opensearch_meta


__all__ = ["OpensearchMetaTemplatetagTest"]  # type: List[str]


class OpensearchMetaTemplatetagTest(TestCase):
    """
    Opensearch meta templatetag tests.
    """

    def test_opensearch_meta__return(self) -> None:
        """
        Test templatetag returning value.

        :return: nothing.
        :rtype: None.
        """

        result = opensearch_meta()  # type: Dict[str, str]
        expected = {
            "OPENSEARCH_DESCRIPTION": settings.OPENSEARCH_DESCRIPTION
        }  # type: Dict[str, str]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_opensearch_meta__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        template = Template(
            "{% load opensearch_tags %}" "{% opensearch_meta %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = '<link rel="search" type="application/opensearchdescription+xml" title="Search engine human-readable text description" href="/opensearch.xml" />'  # noqa: E501, type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(OPENSEARCH_DESCRIPTION="")
    def test_opensearch_meta__render__without_description(self) -> None:
        """
        Test templatetag rendering result without description.

        :return: nothing.
        :rtype: None.
        """

        template = Template(
            "{% load opensearch_tags %}" "{% opensearch_meta %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)
