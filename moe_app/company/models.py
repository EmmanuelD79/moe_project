from django.db import models
from assets.InfoBase import DateTimeInfo, PhoneInfo, AddressInfo, Owner


class CompanyCategory(models.Model):
    name = models.CharField("Nom", max_length=100, blank=False)

    class Meta:
        verbose_name = "Catégorie"
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"


class Company(DateTimeInfo, AddressInfo, PhoneInfo, Owner):
    company_group = models.ForeignKey(
        'self', blank=True, null=True, verbose_name="Groupe", related_name='holding', on_delete=models.PROTECT)
    identification_code = models.CharField("siret", max_length=14, blank=False)
    identification_type = models.CharField(
        "Forme juridique", max_length=10, blank=False)
    legal_name = models.CharField(
        "Nom commercial", max_length=100, blank=False)
    status = models.CharField("Status", max_length=100, blank=True)
    website = models.URLField("Site", max_length=256, blank=True)
    category = models.ForeignKey(
        CompanyCategory, on_delete=models.PROTECT, verbose_name="Catégorie")

    class Meta:
        verbose_name = "Société"
        ordering = ('legal_name',)

    def __str__(self):
        return f"{self.legal_name}"
