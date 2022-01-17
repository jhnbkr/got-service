import json
import os

import django

ENV_VARS = {
    "DJANGO_SETTINGS_MODULE": "project.settings",
}

for key, value in ENV_VARS.items():
    os.environ.setdefault(key, value)

django.setup()

from django.conf import settings

from content.models import Culture, Region, House, Character


def load(filename):
    with open(os.path.join(settings.BASE_DIR, "data", filename)) as file:
        return json.load(file)


character_data = load("characters.json")
house_data = load("houses.json")

# Cultures
culture_names = []
for entry in character_data:
    if entry["Culture"]:
        culture_names.append(entry["Culture"].title())
culture_names = list(sorted(set(culture_names)))

cultures = []
for name in culture_names:
    cultures.append(Culture(name=name))

Culture.objects.bulk_create(cultures)

# Regions
region_names = []
for entry in house_data:
    if entry["Region"] and entry["Region"] != "None":
        region_names.append(entry["Region"].title())
region_names = list(sorted(set(region_names)))

regions = []
for name in region_names:
    regions.append(Region(name=name))

Region.objects.bulk_create(regions)

# Houses
houses = []
for entry in house_data:
    try:
        region = Region.objects.get(name__iexact=entry["Region"])
    except Region.DoesNotExist:
        region = None

    houses.append(
        House(
            id=entry["Id"],
            name=entry["Name"],
            region=region,
            coat_of_arms=entry["CoatOfArms"],
            words=entry["Words"],
            seats=entry["Seats"],
            lord_id=entry["CurrentLord"],
            heir_id=entry["Heir"],
            overlord_id=entry["Overlord"],
            founder_id=entry["Founder"],
            founded=entry["Founded"],
            ancestral_weapons=entry["AncestralWeapons"],
        )
    )

# Characters
characters = []
allegiances = []
for entry in character_data:
    try:
        culture = Culture.objects.get(name__iexact=entry["Culture"])
    except Culture.DoesNotExist:
        culture = None

    if entry["Name"]:
        name = entry["Name"]
    elif len(entry["Aliases"]) > 0:
        name = entry["Aliases"][0]
    else:
        continue

    characters.append(
        Character(
            id=entry["Id"],
            name=name,
            gender=Character.Gender.FEMALE
            if entry["IsFemale"]
            else Character.Gender.MALE,
            culture=culture,
            born=entry["Born"],
            died=entry["Died"],
            titles=entry["Titles"],
            aliases=entry["Aliases"],
            mother_id=entry["Mother"],
            father_id=entry["Father"],
            spouse_id=entry["Spouse"],
        )
    )

    if entry["Allegiances"]:
        for allegiance in entry["Allegiances"]:
            allegiances.append(
                Character.allegiances.through(
                    character_id=entry["Id"], house_id=allegiance
                )
            )

Character.objects.bulk_create(characters)
House.objects.bulk_create(houses)
Character.allegiances.through.objects.bulk_create(allegiances)
