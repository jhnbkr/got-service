from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from api.decorators import cache_request
from api.region.serializers import RegionSerializer
from content.models import Region


class RegionAPIView(GenericAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    search_fields = ["name"]
    ordering_fields = ["name", "num_houses", "created_at"]
    ordering = ["name"]


@method_decorator(cache_request, name="get")
class RegionListView(ListModelMixin, RegionAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@method_decorator(cache_request, name="get")
class RegionRetrieveView(RetrieveModelMixin, RegionAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
