from project.settings.environment import ENV

API_DEFAULT_LIMIT = ENV.int("API_DEFAULT_LIMIT", default=10)
API_MAX_LIMIT = ENV.int("API_MAX_LIMIT", default=100)

# Django REST Framework
# https://www.django-rest-framework.org

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "api.filters.ReversibleOrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "api.pagination.LimitOffsetPagination",
    "DEFAULT_THROTTLE_CLASSES": [],
    "URL_FORMAT_OVERRIDE": None,
    "COERCE_DECIMAL_TO_STRING": False,
}
