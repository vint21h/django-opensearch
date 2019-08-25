# -*- coding: utf-8 -*-

# django-opensearch
# tests/templatetags/test_opensearch_tags.py


from django.template import Context, Template
from django.test import TestCase
from django.test.utils import override_settings

from opensearch.templatetags.opensearch_tags import opensearch_meta


__all__ = ["OpensearchMetaTemplatetagTest"]  # type: list


class OpensearchMetaTemplatetagTest(TestCase):
    """
    Opensearch meta templatetag tests.
    """

    def test_opensearch_meta__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(obj=opensearch_meta(context=context), cls=Context)

    def test_opensearch_meta__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load opensearch_tags %}" "{% opensearch_meta %}")
        response = template.render(context)  # type: str
        expected = '<link rel="search" type="application/opensearchdescription+xml" title="Search engine human-readable text description" href="/opensearch.xml" />'  # noqa: E501, type: str

        self.assertHTMLEqual(html1=response, html2=expected)

    @override_settings(OPENSEARCH_DESCRIPTION="")
    def test_opensearch_meta__render__without_description(self) -> None:
        """
        Test templatetag rendering result without description.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load opensearch_tags %}" "{% opensearch_meta %}")
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)
