from django.contrib import admin
from authentication.admin import moe_site
from company.models import Company, CompanyCategory


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('legal_name', 'category')
    list_filter = ()
    ordering = ("legal_name",)

    fieldsets = (
        (None,
         {'fields': ('legal_name', 'identification_code', 'identification_type')}),
        ('Details Société',
         {'fields': ('company_group', 'status', 'category', 'website',

                     )}),
        ('Coordonées',
         {'fields': ('address', 'city', 'zip_code', 'country', ('phone', 'mobile'))}),
        ('Info supplémentaires',
         {'fields': (('date_updated', 'date_created'),)})
    )

    add_fieldsets = (
        ('Infos Situation', {
            'fields': ('legal_name', 'identification_code', 'identification_type')}),
        ('Details Société',
         {'fields': ('company_group', 'status', 'category', 'website',
                     )}),
        ('Coordonées',
         {'fields': ('address', 'city', 'zip_code', 'country')}),
    )


moe_site.register(Company, CompanyAdmin)
moe_site.register(CompanyCategory)

# Register your models here.
