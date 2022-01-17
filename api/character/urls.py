from django.urls import path

from api.character.views import (
    CharacterListView,
    CharacterRetrieveView,
)

urlpatterns = [
    path("", CharacterListView.as_view(), name="character-list"),
    path("<int:pk>/", CharacterRetrieveView.as_view(), name="character-retrieve"),
]
