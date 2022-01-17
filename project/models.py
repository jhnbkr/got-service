import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from project.validators import TypeValidator


class AbstractModel(models.Model):
    uuid = models.UUIDField(
        _("UUID"),
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
    )
    metadata = models.JSONField(
        _("Metadata"),
        default=dict,
        blank=True,
        null=True,
        validators=[TypeValidator(dict)],
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    @classmethod
    def get_field(cls, field_name):
        return cls._meta.get_field(field_name)

    def silent_save(self, *fields):
        klass = type(self)
        if hasattr(klass, "_default_manager"):
            klass._default_manager.filter(pk=self.pk).update(
                **{
                    field: getattr(self, field)
                    for field in fields
                    if hasattr(self, field)
                }
            )

    class Meta:
        abstract = True
        ordering = ["-created_at"]
