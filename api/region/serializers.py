from rest_framework import serializers

from content.models import Region


class RegionSerializer(serializers.ModelSerializer):
    num_houses = serializers.IntegerField(read_only=True)

    class Meta:
        model = Region
        fields = [
            "id",
            "uuid",
            "name",
            "num_houses",
            "metadata",
            "created_at",
        ]
