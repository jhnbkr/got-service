from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from api.culture.serializers import CultureSerializer
from api.decorators import cache_request
from content.models import Culture


class CultureAPIView(GenericAPIView):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer

    search_fields = ["name"]
    ordering_fields = ["name", "created_at"]
    ordering = ["name"]


@method_decorator(cache_request, name="get")
class CultureListView(ListModelMixin, CultureAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@method_decorator(cache_request, name="get")
class CultureRetrieveView(RetrieveModelMixin, CultureAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
