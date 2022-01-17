from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class VersionView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"version": settings.VERSION}, status=status.HTTP_200_OK)
