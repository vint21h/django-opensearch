.. django-opensearch
.. README.rst

A django-opensearch documentation
=================================

|Travis|_ |Coverage|_ |Codacy|_ |Requires|_ |pypi-license| |pypi-version| |pypi-python-version| |pypi-django-version| |pypi-format| |pypi-wheel| |pypi-status|

    *django-opensearch is a django reusable application to handle opensearch.xml*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``git clone https://github.com/vint21h/django-opensearch.git``. Or download the latest release from https://github.com/vint21h/django-opensearch/tags/.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-opensearch``.

Configuration
-------------
* Add ``"opensearch"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    # settings.py

    INSTALLED_APPS += (
        "opensearch",
    )

* Add ``"opensearch"`` to your URLs definitions.

.. code-block:: python

    # urls.py

    urlpatterns += [
        url(r"^opensearch/", include("opensearch.urls")),
    ]

Usage
-----
Load ``"opensearch_tags"`` to your base template and place opensearch rel meta tag to <head> HTML tag by calling ``{% opensearch_meta %}``.

.. code-block:: django

    {# base.html #}

    {% load opensearch_tags %}

    <head>
        {% opensearch_meta %}
    </head>


django-opensearch settings
--------------------------
``OPENSEARCH_CONTACT_EMAIL``
    Contains an email address at which the maintainer of the description document can be reached. Defaults to ``""``.

``OPENSEARCH_SHORT_NAME``
    Contains a brief human-readable title that identifies this search engine. Defaults to ``""``.

``OPENSEARCH_DESCRIPTION``
    Contains a human-readable text description of the search engine. Defaults to ``""``.

``OPENSEARCH_FAVICON_WIDTH``
    Contains width of an image that can be used in association with this search content. Defaults to ``16``.

``OPENSEARCH_FAVICON_HEIGHT``
    Contains height of an image that can be used in association with this search content. Defaults to ``16``.

``OPENSEARCH_FAVICON_TYPE``
    Contains mimetype of an image that can be used in association with this search content. Defaults to ``"image/x-icon"``.

``OPENSEARCH_FAVICON_FILE``
    Contains a URL that identifies the location of an image that can be used in association with this search content. Defaults to ``"favicon.ico"``.

``OPENSEARCH_SEARCH_URL``
    Contains a django URL name to search content. Defaults to ``"search"``.

``OPENSEARCH_SEARCH_QUERYSTRING``
    Contains the querystring to prepend to search parameter. Defaults to ``"q="``.

``OPENSEARCH_INPUT_ENCODING``
    Contains a string that indicates that the search engine supports search requests encoded with the specified character encoding. Defaults to ``"UTF-8"``.


Licensing
---------
django-opensearch is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-opensearch/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.

.. |Travis| image:: https://travis-ci.org/vint21h/django-opensearch.svg?branch=master
.. |Coverage| image:: https://api.codacy.com/project/badge/Coverage/c4c5db8aa2684496a08412f734395c19
.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/c4c5db8aa2684496a08412f734395c19
.. |Requires| image:: https://requires.io/github/vint21h/django-opensearch/requirements.svg?branch=master
.. |pypi-license| image:: https://img.shields.io/pypi/l/django-opensearch
.. |pypi-version| image:: https://img.shields.io/pypi/v/django-opensearch
.. |pypi-django-version| image:: https://img.shields.io/pypi/djversions/django-opensearch
.. |pypi-python-version| image:: https://img.shields.io/pypi/pyversions/django-opensearch
.. |pypi-format| image:: https://img.shields.io/pypi/format/django-opensearch
.. |pypi-wheel| image:: https://img.shields.io/pypi/wheel/django-opensearch
.. |pypi-status| image:: https://img.shields.io/pypi/status/django-opensearch
.. _Travis: https://travis-ci.org/vint21h/django-opensearch/
.. _Coverage: https://www.codacy.com/app/vint21h/django-opensearch
.. _Codacy: https://www.codacy.com/app/vint21h/django-opensearch
.. _Requires: https://requires.io/github/vint21h/django-opensearch/requirements/?branch=master
