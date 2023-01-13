from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from django.conf import settings


class DateTimeInfo(models.Model):
    date_created = models.DateTimeField("Crée le", auto_now_add=True)
    date_updated = models.DateTimeField("Mise à jour le", auto_now=True)

    class Meta:
        abstract = True


class Owner(models.Model):
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.PROTECT, verbose_name="Propriétaire")

    class Meta:
        abstract = True


class PhoneInfo(models.Model):
    phone = models.CharField(
        "Téléphone",
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
        blank=True,
    )
    mobile = models.CharField(
        "Portable",
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
        blank=True
    )

    class Meta:
        abstract = True


class AddressInfo(models.Model):
    address = models.CharField(
        "Adresse",
        max_length=200,
        blank=True
    )

    city = models.CharField(
        "Ville",
        max_length=200,
        blank=True
    )
    zip_code = models.PositiveIntegerField(verbose_name="Code postal", blank=True, null=True,
                                           validators=[
                                               MaxValueValidator(99999)]
                                           )
    country = models.CharField(
        "Pays",
        max_length=50,
        blank=True
    )

    class Meta:
        abstract = True


class ContactInfo(models.Model):
    email = models.EmailField("Email", max_length=256,
                              blank=False, unique=True)
    first_name = models.CharField("Prénom", max_length=256, blank=False)
    last_name = models.CharField("Nom", max_length=256, blank=False)
    birthday = models.DateField("Né(e) le", blank=True, null=True)
    title = models.CharField("Poste", max_length=256, blank=True)
    url = models.URLField("Url", max_length=256, blank=True, null=True)
    photo_original = models.ImageField(
        upload_to='photo_profil/', blank=True, null=True, verbose_name="Photo de profil")
    time_zone_identifier = models.CharField("UTC", max_length=10, blank=True)

    class Meta:
        abstract = True
