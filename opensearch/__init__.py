# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/__init__.py


from typing import List


__all__ = ["default_app_config"]  # type: List[str]


default_app_config = "opensearch.apps.DjangoOpensearchConfig"  # type: str
