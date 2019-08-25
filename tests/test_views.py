# -*- coding: utf-8 -*-

# django-opensearch
# tests/test_views.py


from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse
from django.utils import translation

from opensearch.views import opensearch


__all__ = ["OpensearchViewTest"]  # type: list


class OpensearchViewTest(TestCase):
    """
    opensearch.xml view tests.
    """

    def test_humans_txt__return_response(self) -> None:
        """
        Test view returning response.

        :return: nothing.
        :rtype: None.
        """

        request = HttpRequest()

        self.assertIsInstance(obj=opensearch(request=request), cls=HttpResponse)

    def test_opensearch__render__template_used(self) -> None:
        """
        Test view right template usage .

        :return: nothing.
        :rtype: None.
        """

        with translation.override("en"):
            response = self.client.get(path=reverse("opensearch"))

        self.assertTemplateUsed(
            response=response, template_name="opensearch/opensearch.xml"
        )

    def test_opensearch__render(self) -> None:
        """
        Test view rendering result.

        :return: nothing.
        :rtype: None.
        """

        expected = """"""  # type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("opensearch"))

        self.assertIsNotNone(obj=response.context.get("OPENSEARCH_DESCRIPTION"))
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    @override_settings(OPENSEARCH_DESCRIPTION="")
    def test_opensearch__render__without_banner(self) -> None:
        """
        Test view rendering result without description.

        :return: nothing.
        :rtype: None.
        """

        expected = """"""  # type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("opensearch"))

        self.assertEqual(
            first="", second=response.context.get("OPENSEARCH_DESCRIPTION")
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)
