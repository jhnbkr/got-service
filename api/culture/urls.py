from django.urls import path

from api.culture.views import (
    CultureListView,
    CultureRetrieveView,
)

urlpatterns = [
    path("", CultureListView.as_view(), name="culture-list"),
    path("<int:pk>/", CultureRetrieveView.as_view(), name="culture-retrieve"),
]
