from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from api.character.filters import CharacterFilter
from api.character.serializers import CharacterSerializer
from api.decorators import cache_request
from content.models import Character


class CharacterAPIView(GenericAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filterset_class = CharacterFilter

    search_fields = ["name", "aliases"]
    ordering_fields = ["name", "created_at"]
    ordering = ["name"]


@method_decorator(cache_request, name="get")
class CharacterListView(ListModelMixin, CharacterAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@method_decorator(cache_request, name="get")
class CharacterRetrieveView(RetrieveModelMixin, CharacterAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
