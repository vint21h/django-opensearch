# -*- coding: utf-8 -*-

# django-opensearch
# tests/test_views.py


from django.conf.urls import url, include
from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.utils import translation

from opensearch.views import opensearch


__all__ = ["OpensearchViewTest"]  # type: list


def search(request: HttpRequest) -> HttpResponse:
    """
    Fake search view.

    :param request: django request instance.
    :type request: django.http.request.HttpRequest.
    :return: rendered opensearch.xml
    :rtype: django.http.HttpResponse.
    """

    return HttpResponse()


urlpatterns = [
    url(r"^search$", search, name="search")  # fake search view
]  # type: list
urlpatterns += [url(r"^opensearch/", include("opensearch.urls"))]


@override_settings(ROOT_URLCONF="tests.test_views")
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
        request.META.update({"SERVER_NAME": "example.com", "SERVER_PORT": 80})

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

        expected = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <ShortName>opensearch</ShortName>
            <Description>Search engine human-readable text description</Description>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """  # type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("opensearch"))

        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    @override_settings(OPENSEARCH_CONTACT_EMAIL="")
    def test_opensearch__render__without_email(self) -> None:
        """
        Test view rendering result without contact email.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <ShortName>opensearch</ShortName>
            <Description>Search engine human-readable text description</Description>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """  # type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("opensearch"))

        self.assertEqual(
            first=response.context.get("OPENSEARCH_CONTACT_EMAIL"), second=""
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    @override_settings(OPENSEARCH_SHORT_NAME="")
    def test_opensearch__render__without_name(self) -> None:
        """
        Test view rendering result without short name.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <Description>Search engine human-readable text description</Description>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """  # type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("opensearch"))

        self.assertEqual(first=response.context.get("OPENSEARCH_SHORT_NAME"), second="")
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    @override_settings(OPENSEARCH_DESCRIPTION="")
    def test_opensearch__render__without_description(self) -> None:
        """
        Test view rendering result without description.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <ShortName>opensearch</ShortName>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """  # type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("opensearch"))

        self.assertEqual(
            first=response.context.get("OPENSEARCH_DESCRIPTION"), second=""
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    @override_settings(
        OPENSEARCH_FAVICON_WIDTH=0,
        OPENSEARCH_FAVICON_HEIGHT=0,
        OPENSEARCH_FAVICON_TYPE="",
        OPENSEARCH_FAVICON_FILE="",
    )
    def test_opensearch__render__without_favicon(self) -> None:
        """
        Test view rendering result without favicon.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <ShortName>opensearch</ShortName>
            <Description>Search engine human-readable text description</Description>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
            <InputEncoding>UTF-8</InputEncoding>
        </OpenSearchDescription>
        """  # type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("opensearch"))

        self.assertEqual(
            first=response.context.get("OPENSEARCH_FAVICON_WIDTH"), second=0
        )
        self.assertEqual(
            first=response.context.get("OPENSEARCH_FAVICON_HEIGHT"), second=0
        )
        self.assertEqual(
            first=response.context.get("OPENSEARCH_FAVICON_TYPE"), second=""
        )
        self.assertEqual(
            first=response.context.get("OPENSEARCH_FAVICON_FILE"), second=""
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    @override_settings(OPENSEARCH_SEARCH_URL="", OPENSEARCH_SEARCH_QUERYSTRING="")
    def test_opensearch__render__without_url(self) -> None:
        """
        Test view rendering result without url.
        Must raise no reverse match error for empty URL name.

        :return: nothing.
        :rtype: None.
        """

        with translation.override("en"):
            with self.assertRaises(expected_exception=NoReverseMatch):
                self.client.get(path=reverse("opensearch"))

    @override_settings(OPENSEARCH_INPUT_ENCODING="")
    def test_opensearch__render__without_encoding(self) -> None:
        """
        Test view rendering result without input encoding.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
            <Contact>test@example.com</Contact>
            <ShortName>opensearch</ShortName>
            <Description>Search engine human-readable text description</Description>
            <Image width="16" height="16" type="image/x-icon">favicon.ico</Image>
            <Url type="text/html" template="http://testserver/search?q={searchTerms}"/>
        </OpenSearchDescription>
        """  # type: str

        with translation.override("en"):
            response = self.client.get(path=reverse("opensearch"))

        self.assertEqual(
            first=response.context.get("OPENSEARCH_INPUT_ENCODING"), second=""
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)
