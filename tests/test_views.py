# -*- coding: utf-8 -*-

# django-opensearch
# tests/test_views.py


from typing import List, Union

from django.test import TestCase
from django.shortcuts import resolve_url
from django.urls import include, re_path
from django.test.utils import override_settings
from django.http import HttpRequest, HttpResponse
from django.urls.exceptions import NoReverseMatch
from django.urls.resolvers import URLPattern, URLResolver
from django.utils.translation import override as override_translation

from opensearch.views import opensearch


__all__: List[str] = ["OpensearchViewTest"]


def search(request: HttpRequest) -> HttpResponse:
    """
    Fake search view.

    :param request: django request instance
    :type request: HttpRequest
    :return: rendered opensearch.xml
    :rtype: HttpResponse
    """
    return HttpResponse()


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    re_path(r"^search$", search, name="search")  # fake search view
]
urlpatterns += [re_path(r"^opensearch/", include("opensearch.urls"))]


@override_settings(ROOT_URLCONF="tests.test_views")
class OpensearchViewTest(TestCase):
    """opensearch.xml view tests."""

    def test_humans_txt__return_response(self) -> None:
        """Test view returning response."""
        request: HttpRequest = HttpRequest()
        request.META.update({"SERVER_NAME": "example.com", "SERVER_PORT": 80})

        self.assertIsInstance(obj=opensearch(request=request), cls=HttpResponse)

    @override_translation(language="en")
    def test_opensearch__render__template_used(self) -> None:
        """Test view right template usage."""
        result: HttpResponse = self.client.get(
            path=resolve_url(to="opensearch")
        )

        self.assertTemplateUsed(
            response=result, template_name="opensearch/opensearch.xml"
        )

    @override_translation(language="en")
    def test_opensearch__render(self) -> None:
        """Test view rendering result."""
        expected: str = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <ShortName>opensearch</ShortName>
            <Description>Search engine human-readable text description</Description>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """
        result: HttpResponse = self.client.get(
            path=resolve_url(to="opensearch")
        )

        self.assertXMLEqual(xml1=result.content.decode(), xml2=expected)

    @override_settings(OPENSEARCH_CONTACT_EMAIL="")
    @override_translation(language="en")
    def test_opensearch__render__without_email(self) -> None:
        """Test view rendering result without contact email."""
        expected: str = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <ShortName>opensearch</ShortName>
            <Description>Search engine human-readable text description</Description>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """
        result: HttpResponse = self.client.get(
            path=resolve_url(to="opensearch")
        )

        self.assertEqual(
            first=result.context.get("OPENSEARCH_CONTACT_EMAIL")
            if result.context
            else None,
            second="",
        )
        self.assertXMLEqual(xml1=result.content.decode(), xml2=expected)

    @override_settings(OPENSEARCH_SHORT_NAME="")
    @override_translation(language="en")
    def test_opensearch__render__without_name(self) -> None:
        """Test view rendering result without short name."""
        expected: str = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <Description>Search engine human-readable text description</Description>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """
        result: HttpResponse = self.client.get(
            path=resolve_url(to="opensearch")
        )

        self.assertEqual(
            first=result.context.get("OPENSEARCH_SHORT_NAME")
            if result.context
            else None,
            second="",
        )
        self.assertXMLEqual(xml1=result.content.decode(), xml2=expected)

    @override_settings(OPENSEARCH_DESCRIPTION="")
    @override_translation(language="en")
    def test_opensearch__render__without_description(self) -> None:
        """Test view rendering result without description."""
        expected: str = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <ShortName>opensearch</ShortName>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """
        result: HttpResponse = self.client.get(
            path=resolve_url(to="opensearch")
        )

        self.assertEqual(
            first=result.context.get("OPENSEARCH_DESCRIPTION")
            if result.context
            else None,
            second="",
        )
        self.assertXMLEqual(xml1=result.content.decode(), xml2=expected)

    @override_settings(
        OPENSEARCH_FAVICON_WIDTH=0,
        OPENSEARCH_FAVICON_HEIGHT=0,
        OPENSEARCH_FAVICON_TYPE="",
        OPENSEARCH_FAVICON_FILE="",
    )
    @override_translation(language="en")
    def test_opensearch__render__without_favicon(self) -> None:
        """Test view rendering result without favicon."""
        expected: str = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <ShortName>opensearch</ShortName>
            <Description>Search engine human-readable text description</Description>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """
        result: HttpResponse = self.client.get(
            path=resolve_url(to="opensearch")
        )

        self.assertEqual(
            first=result.context.get("OPENSEARCH_FAVICON_WIDTH")
            if result.context
            else None,
            second=0,
        )
        self.assertEqual(
            first=result.context.get("OPENSEARCH_FAVICON_HEIGHT")
            if result.context
            else None,
            second=0,
        )
        self.assertEqual(
            first=result.context.get("OPENSEARCH_FAVICON_TYPE")
            if result.context
            else None,
            second="",
        )
        self.assertEqual(
            first=result.context.get("OPENSEARCH_FAVICON_FILE")
            if result.context
            else None,
            second="",
        )
        self.assertXMLEqual(xml1=result.content.decode(), xml2=expected)

    @override_settings(OPENSEARCH_SEARCH_URL="", OPENSEARCH_SEARCH_QUERYSTRING="")
    @override_translation(language="en")
    def test_opensearch__render__without_url(self) -> None:
        """
        Test view rendering result without url.

        Must raise no reverse match error for empty URL name.
        """
        with self.assertRaises(expected_exception=NoReverseMatch):
            self.client.get(path=resolve_url(to="opensearch"))

    @override_settings(OPENSEARCH_INPUT_ENCODING="")
    @override_translation(language="en")
    def test_opensearch__render__without_encoding(self) -> None:
        """Test view rendering result without input encoding."""
        expected: str = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <ShortName>opensearch</ShortName>
            <Description>Search engine human-readable text description</Description>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
        </OpenSearchDescription>
        """

        result: HttpResponse = self.client.get(
            path=resolve_url(to="opensearch")
        )

        self.assertEqual(
            first=result.context.get("OPENSEARCH_INPUT_ENCODING")
            if result.context
            else None,
            second="",
        )
        self.assertXMLEqual(xml1=result.content.decode(), xml2=expected)
