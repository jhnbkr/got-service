from django.urls import include, path

from api.version.views import VersionView

urlpatterns = [
    path("character/", include("api.character.urls")),
    path("culture/", include("api.culture.urls")),
    path("house/", include("api.house.urls")),
    path("region/", include("api.region.urls")),
    path("version/", VersionView.as_view()),
]
