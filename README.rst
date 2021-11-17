.. django-opensearch
.. README.rst


A django-opensearch documentation
=================================

|GitHub|_ |Coveralls|_ |pypi-license|_ |pypi-version|_ |pypi-python-version|_ |pypi-django-version|_ |pypi-format|_ |pypi-wheel|_ |pypi-status|_

    *django-opensearch is a Django reusable application to handle opensearch.xml*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``$ git clone https://github.com/vint21h/django-opensearch.git``. Or download the latest release from https://github.com/vint21h/django-opensearch/tags/.
* Run ``$ python ./setup.py install`` from the repository source tree or unpacked archive. Or use pip: ``$ pip install django-opensearch``.

Configuration
-------------
* Add ``"opensearch"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    # settings.py

    INSTALLED_APPS += [
        "opensearch",
    ]

* Add ``"opensearch"`` to your URLs definitions.

.. code-block:: python

    # urls.py

    from django.urls import re_path


    urlpatterns += [
        re_path(r"^opensearch/", include("opensearch.urls")),
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

Settings
--------
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
    Contains a Django URL name to search content. Defaults to ``"search"``.

``OPENSEARCH_SEARCH_QUERYSTRING``
    Contains the querystring to prepend to search parameter. Defaults to ``"q="``.

``OPENSEARCH_INPUT_ENCODING``
    Contains a string that indicates that the search engine supports search requests encoded with the specified character encoding. Defaults to ``"UTF-8"``.

Contributing
------------
1. `Fork it <https://github.com/vint21h/django-opensearch/>`_
2. Install `GNU Make <https://www.gnu.org/software/make/>`_
3. Install and configure `pyenv <https://github.com/pyenv/pyenv/>`_ and `pyenv-virtualenv plugin <https://github.com/pyenv/pyenv-virtualenv/>`_
4. Install and configure `direnv <https://github.com/direnv/direnv/>`_
5. Create environment config from example

.. code-block:: bash

    cp .env.example .env

6. Install development dependencies:

.. code-block:: bash

    make install

7. Create your fix/feature branch:

.. code-block:: bash

    git checkout -b my-new-fix-or-feature

8. Check code style and moreover:

.. code-block:: bash

    make check

9. Run tests:

.. code-block:: bash

    make test

10. Push to the branch:

.. code-block:: bash

    git push origin my-new-fix-or-feature

11. `Create a new Pull Request <https://github.com/vint21h/django-opensearch/compare/>`_

Licensing
---------
django-opensearch is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-opensearch/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.

.. |GitHub| image:: https://github.com/vint21h/django-opensearch/workflows/build/badge.svg
    :alt: GitHub
.. |Coveralls| image:: https://coveralls.io/repos/github/vint21h/django-opensearch/badge.svg?branch=master
    :alt: Coverage
.. |pypi-license| image:: https://img.shields.io/pypi/l/django-opensearch
    :alt: License
.. |pypi-version| image:: https://img.shields.io/pypi/v/django-opensearch
    :alt: Version
.. |pypi-django-version| image:: https://img.shields.io/pypi/djversions/django-opensearch
    :alt: Supported Django version
.. |pypi-python-version| image:: https://img.shields.io/pypi/pyversions/django-opensearch
    :alt: Supported Python version
.. |pypi-format| image:: https://img.shields.io/pypi/format/django-opensearch
    :alt: Package format
.. |pypi-wheel| image:: https://img.shields.io/pypi/wheel/django-opensearch
    :alt: Python wheel support
.. |pypi-status| image:: https://img.shields.io/pypi/status/django-opensearch
    :alt: Package status
.. _GitHub: https://github.com/vint21h/django-opensearch/actions/
.. _Coveralls: https://coveralls.io/github/vint21h/django-opensearch?branch=master
.. _pypi-license: https://pypi.org/project/django-opensearch/
.. _pypi-version: https://pypi.org/project/django-opensearch/
.. _pypi-django-version: https://pypi.org/project/django-opensearch/
.. _pypi-python-version: https://pypi.org/project/django-opensearch/
.. _pypi-format: https://pypi.org/project/django-opensearch/
.. _pypi-wheel: https://pypi.org/project/django-opensearch/
.. _pypi-status: https://pypi.org/project/django-opensearch/
