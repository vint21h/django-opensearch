.. django-opensearch
.. README.rst

A django-opensearch documentation
=================================

    *django-opensearch is a django reusable application to handle opensearch.xml*

.. contents::

Installation
------------
* Obtain your copy of source code from git repository: ``git clone https://github.com/vint21h/django-opensearch.git``. Or download latest release from https://github.com/vint21h/django-opensearch/tags.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-opensearch``.

Configuration
-------------
Add ``'opensearch'`` to ``settings.INSTALLED_APPS``.

    INSTALLED_APPS = (
        ...,

        'opensearch',

        ...,

    )

Add ``'opensearch'`` to your urls definitions.

    urlpatterns = patterns('',
        ...,

        url(r'^opensearch/', include('opensearch.urls')),

        ...,

    )

Load ``'opensearch_tags'`` to your base template and place opensearch rel meta tag to <head> html tag by calling ``{% opensearch_meta %}``.

Opensearch settings
-------------------
``OPENSEARCH_CONTACT_EMAIL``
    Contains an email address at which the maintainer of the description document can be reached. Defaults to ``u''``.

``OPENSEARCH_SHORT_NAME``
    Contains a brief human-readable title that identifies this search engine. Defaults to ``u''``.

``OPENSEARCH_DESCRIPTION``
    Contains a human-readable text description of the search engine. Defaults to ``u''``.

``OPENSEARCH_FAVICON_WIDTH``
    Contains width of an image that can be used in association with this search content. Defaults to ``16``.

``OPENSEARCH_FAVICON_HEIGHT``
    Contains height of an image that can be used in association with this search content. Defaults to ``16``.

``OPENSEARCH_FAVICON_TYPE``
    Contains mimetype of an image that can be used in association with this search content. Defaults to ``u'image/x-icon'``.

``OPENSEARCH_FAVICON_FILE``
    Contains a URL that identifies the location of an image that can be used in association with this search content. Defaults to ``u'favicon.ico'``.

``OPENSEARCH_SEARCH_URL``
    Contains a django URL name to search content. Defaults to ``u'search'``.


Licensing
---------
django-opensearch is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-opensearch

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>
