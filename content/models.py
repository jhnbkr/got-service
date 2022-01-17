from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from project.models import AbstractModel


class Culture(AbstractModel):
    name = models.CharField(_("Name"), unique=True, max_length=256)

    def __str__(self):
        return str(self.name)

    class Meta(AbstractModel.Meta):
        ordering = ["name"]
        verbose_name = _("Culture")
        verbose_name_plural = _("Cultures")


class RegionManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().annotate(num_houses=Count("houses", distinct=True))
        )


class Region(AbstractModel):
    name = models.CharField(_("Name"), unique=True, max_length=256)

    objects = RegionManager()

    def __str__(self):
        return str(self.name)

    class Meta(AbstractModel.Meta):
        ordering = ["name"]
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")


class HouseManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related(
                "region",
                "founder",
                "founder__culture",
                "lord",
                "lord__culture",
                "heir",
                "heir__culture",
                "overlord",
                "overlord__culture",
            )
        )


class House(AbstractModel):
    name = models.CharField(_("Name"), max_length=256)
    region = models.ForeignKey(
        Region,
        verbose_name=_("Region"),
        related_name="houses",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    coat_of_arms = models.CharField(_("Coat of Arms"), max_length=256, blank=True)
    words = models.CharField(_("words"), max_length=256, blank=True)
    founded = models.CharField(_("founded"), max_length=256, blank=True)
    founder = models.ForeignKey(
        "Character",
        verbose_name=_("Founder"),
        related_name="founder_of",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    lord = models.ForeignKey(
        "Character",
        verbose_name=_("Lord"),
        related_name="lord_of",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    heir = models.ForeignKey(
        "Character",
        verbose_name=_("Heir"),
        related_name="heir_of",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    overlord = models.ForeignKey(
        "Character",
        verbose_name=_("Overlord"),
        related_name="overlord_of",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    seats = ArrayField(
        models.CharField(max_length=256), verbose_name=_("Seats"), blank=True, null=True
    )
    ancestral_weapons = ArrayField(
        models.CharField(max_length=256),
        verbose_name=_("Ancestral Weapons"),
        blank=True,
        null=True,
    )

    objects = HouseManager()

    def __str__(self):
        return str(self.name)

    class Meta(AbstractModel.Meta):
        ordering = ["name"]
        verbose_name = _("House")
        verbose_name_plural = _("Houses")


class CharacterManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related(
                "culture",
                "mother",
                "mother__culture",
                "father",
                "father__culture",
                "spouse",
                "spouse__culture",
            )
            .prefetch_related("allegiances")
        )


class Character(AbstractModel):
    class Gender(models.TextChoices):
        MALE = "male", _("Male")
        FEMALE = "female", _("Female")
        OTHER = "other", _("Other")

    name = models.CharField(_("Name"), max_length=256)
    gender = models.CharField(_("Gender"), max_length=32, choices=Gender.choices)
    culture = models.ForeignKey(
        Culture,
        verbose_name=_("Culture"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    born = models.CharField(_("Born"), max_length=256, blank=True)
    died = models.CharField(_("Died"), max_length=256, blank=True)
    mother = models.ForeignKey(
        "self",
        verbose_name=_("Mother"),
        related_name="mother_of",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    father = models.ForeignKey(
        "self",
        verbose_name=_("Father"),
        related_name="father_of",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    spouse = models.ForeignKey(
        "self",
        verbose_name=_("Spouse"),
        related_name="spouse_of",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    allegiances = models.ManyToManyField(
        House, verbose_name=_("Allegiances"), blank=True
    )
    titles = ArrayField(
        models.CharField(max_length=256),
        verbose_name=_("Titles"),
        blank=True,
        null=True,
    )
    aliases = ArrayField(
        models.CharField(max_length=256),
        verbose_name=_("Aliases"),
        blank=True,
        null=True,
    )

    objects = CharacterManager()

    def __str__(self):
        return str(self.name)

    class Meta(AbstractModel.Meta):
        ordering = ["name"]
        verbose_name = _("Character")
        verbose_name_plural = _("Characters")
