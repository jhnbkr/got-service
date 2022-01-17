from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from api.decorators import cache_request
from api.house.filters import HouseFilter
from api.house.serializers import HouseSerializer
from content.models import House


class HouseAPIView(GenericAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filterset_class = HouseFilter

    search_fields = ["name"]
    ordering_fields = ["name", "created_at"]
    ordering = ["name"]


@method_decorator(cache_request, name="get")
class HouseListView(ListModelMixin, HouseAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@method_decorator(cache_request, name="get")
class HouseRetrieveView(RetrieveModelMixin, HouseAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
