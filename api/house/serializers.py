from rest_framework import serializers

from api.character.serializers import CharacterBasicSerializer
from api.region.serializers import RegionSerializer
from content.models import House


class HouseSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    founder = CharacterBasicSerializer(read_only=True)
    lord = CharacterBasicSerializer(read_only=True)
    heir = CharacterBasicSerializer(read_only=True)
    overlord = CharacterBasicSerializer(read_only=True)

    class Meta:
        model = House
        fields = [
            "id",
            "uuid",
            "name",
            "region",
            "coat_of_arms",
            "words",
            "founded",
            "founder",
            "lord",
            "heir",
            "overlord",
            "seats",
            "ancestral_weapons",
            "metadata",
            "created_at",
        ]
