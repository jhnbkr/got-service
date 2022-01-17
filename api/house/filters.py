from api import filters
from content.models import House


class HouseFilter(filters.FilterSet):
    region = filters.NumberInFilter(field_name="region")
    founder = filters.NumberInFilter(field_name="founder")
    lord = filters.NumberInFilter(field_name="lord")
    heir = filters.NumberInFilter(field_name="heir")
    overlord = filters.NumberInFilter(field_name="overlord")

    class Meta:
        model = House
        fields = ["region", "founder", "lord", "heir", "overlord"]
