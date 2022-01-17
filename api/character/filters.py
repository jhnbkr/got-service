from api import filters
from content.models import Character


class CharacterFilter(filters.FilterSet):
    culture = filters.NumberInFilter(field_name="culture")
    gender = filters.CharInFilter(field_name="gender")
    mother = filters.NumberInFilter(field_name="mother")
    father = filters.NumberInFilter(field_name="father")
    spouse = filters.NumberInFilter(field_name="spouse")
    allegiances = filters.M2MInFilter(field_name="allegiances__pk")

    class Meta:
        model = Character
        fields = ["culture", "gender", "mother", "father", "spouse", "allegiances"]
