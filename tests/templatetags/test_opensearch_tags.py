# -*- coding: utf-8 -*-

# django-opensearch
# tests/templatetags/test_opensearch_tags.py


from django.template import Context, Template
from django.test import TestCase
from django.test.utils import override_settings


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

        ...

    def test_opensearch_meta__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        ...
