from rest_framework import serializers

from api.culture.serializers import CultureSerializer
from content.models import Character


class CharacterBasicSerializer(serializers.ModelSerializer):
    culture = CultureSerializer(read_only=True)
    mother = serializers.HyperlinkedRelatedField(
        view_name="character-retrieve", read_only=True
    )
    father = serializers.HyperlinkedRelatedField(
        view_name="character-retrieve", read_only=True
    )
    spouse = serializers.HyperlinkedRelatedField(
        view_name="character-retrieve", read_only=True
    )

    class Meta:
        model = Character
        fields = [
            "id",
            "uuid",
            "name",
            "gender",
            "culture",
            "born",
            "died",
            "mother",
            "father",
            "spouse",
            "titles",
            "aliases",
            "metadata",
            "created_at",
        ]


class CharacterSerializer(serializers.ModelSerializer):
    culture = CultureSerializer(read_only=True)
    mother = CharacterBasicSerializer(read_only=True)
    father = CharacterBasicSerializer(read_only=True)
    spouse = CharacterBasicSerializer(read_only=True)
    allegiances = serializers.HyperlinkedRelatedField(
        view_name="house-retrieve", many=True, read_only=True
    )

    class Meta:
        model = Character
        fields = [
            "id",
            "uuid",
            "name",
            "gender",
            "culture",
            "born",
            "died",
            "mother",
            "father",
            "spouse",
            "allegiances",
            "titles",
            "aliases",
            "metadata",
            "created_at",
        ]
