# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/__init__.py


from typing import List


__all__: List[str] = ["default_app_config"]


default_app_config: str = "opensearch.apps.DjangoOpensearchConfig"
