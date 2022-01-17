from collections import OrderedDict

from django.conf import settings
from rest_framework.pagination import LimitOffsetPagination as BaseLimitOffsetPagination
from rest_framework.response import Response


class LimitOffsetPagination(BaseLimitOffsetPagination):
    default_limit = settings.API_DEFAULT_LIMIT
    max_limit = settings.API_MAX_LIMIT

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.count),
                    ("limit", self.limit),
                    ("offset", self.offset),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            )
        )

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                    "example": 123,
                },
                "limit": {
                    "type": "integer",
                    "example": 123,
                },
                "offset": {
                    "type": "integer",
                    "example": 123,
                },
                "next": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": f"http://api.example.org/accounts/?{self.offset_query_param}=400&{self.limit_query_param}=100",
                },
                "previous": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": f"http://api.example.org/accounts/?{self.offset_query_param}=400&{self.limit_query_param}=100",
                },
                "results": schema,
            },
        }
