from rest_framework import serializers

from content.models import Culture


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = [
            "id",
            "uuid",
            "name",
            "metadata",
            "created_at",
        ]
