from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from project.fields import CIEmailField
from project.models import AbstractModel


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Users must have a email address")

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email, password, **kwargs)


class User(AbstractModel, AbstractBaseUser):
    email = CIEmailField(_("Email"), unique=True, db_index=True, max_length=128)
    password = models.CharField(_("Password"), max_length=128)
    name = models.CharField(_("Name"), max_length=64)
    is_active = models.BooleanField(_("Active"), default=True)
    last_login = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    @property
    def is_admin(self):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_admin

    def has_module_perms(self, app_label):
        return self.is_active and self.is_admin

    def get_all_permissions(self, obj=None):
        return []

    class Meta(AbstractModel.Meta):
        verbose_name = _("User")
        verbose_name_plural = _("Users")
