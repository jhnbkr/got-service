from django.urls import path

from api.house.views import (
    HouseListView,
    HouseRetrieveView,
)

urlpatterns = [
    path("", HouseListView.as_view(), name="house-list"),
    path("<int:pk>/", HouseRetrieveView.as_view(), name="house-retrieve"),
]
