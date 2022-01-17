from django.urls import path

from api.region.views import (
    RegionListView,
    RegionRetrieveView,
)

urlpatterns = [
    path("", RegionListView.as_view(), name="region-list"),
    path("<int:pk>/", RegionRetrieveView.as_view(), name="region-retrieve"),
]
