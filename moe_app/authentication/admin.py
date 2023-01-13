from django.contrib import admin
from authentication.models import User, Contact
from django.contrib.auth.forms import UserChangeForm, AdminPasswordChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class MoeAdminArea(admin.AdminSite):
    site_header = 'MOE GESTION PROJET'


class AdminUser(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('id','full_name', 'email', 'phone', 'mobile')
    list_filter = ()
    ordering = ("email",)

    fieldsets = (
        (None,
         {'fields': ('email', 'password', 'photo_original')}),
        ('Details Utilisateur',
         {'fields': (('first_name', 'last_name'), 'title',
                     ('phone', 'mobile'), 'birthday',
                     )}),
        ('Coordonées',
         {'fields': ('address', 'city', 'zip_code', 'country')}),
        ('Info',
         {'fields': ('company', 'time_zone_identifier', 'date_created', 'date_updated', )})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
        ('Infos Utilisateur', {
            'fields': (('first_name', 'last_name'), 'title',
                       ('phone', 'mobile'), 'birthday',)}),
        ('Coordonées',
         {'fields': ('address', 'city', 'zip_code', 'country')}),
        ('Info supplémentaire',
         {'fields': ('company', 'time_zone_identifier')})
    )

    def full_name(self, instance):
        return f"{instance.last_name.upper()}  {instance.first_name.capitalize()}"

    full_name.short_description = "Utilisateur"
    full_name.admin_order_field = "last_name"


class AdminContact(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('full_name', 'email', 'company', 'phone', 'mobile')
    list_filter = ()
    ordering = ("email",)

    fieldsets = (
        (None,
         {'fields': ('email', 'photo_original')}),
        ('Details Utilisateur',
         {'fields': (('first_name', 'last_name'), 'title',
                     ('phone', 'mobile'), 'birthday',
                     )}),
        ('Coordonées',
         {'fields': ('address', 'city', 'zip_code', 'country')}),
        ('Info',
         {'fields': ('company', 'owner', 'time_zone_identifier', 'sub_type', 'is_private', 'date_created', 'date_updated', )})
    )

    add_fieldsets = (
        ('Infos Utilisateur', {
            'fields': (('first_name', 'last_name'), 'email', 'title',
                       ('phone', 'mobile'), 'birthday',)}),
        ('Coordonées',
         {'fields': ('address', 'city', 'zip_code', 'country')}),
        ('Info supplémentaire',
         {'fields': ('company', 'owner', 'time_zone_identifier', 'sub_type', 'is_private')})
    )

    def full_name(self, instance):
        return f"{instance.last_name.upper()}  {instance.first_name.capitalize()}"

    full_name.short_description = "Contact"
    full_name.admin_order_field = "last_name"


moe_site = MoeAdminArea(name='MoeAdmin')
moe_site.register(User, AdminUser)
moe_site.register(Contact, AdminContact)
