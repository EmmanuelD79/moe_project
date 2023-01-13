from django.contrib import admin
from authentication.admin import moe_site
from project.models import Phase, Plan, Project, Task, Lot, TypeLot, FinancialStatus, LotPenalty, ProjectPenalty, PenaltyType


class ProjectPenaltiesInLine(admin.TabularInline):
    model = ProjectPenalty
    
class LotPenaltisInLine(admin.TabularInline):
    model = LotPenalty


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('title', 'company', 'delivery_date', 'amount')
    list_filter = ()
    ordering = ("title",)

    inlines = [ProjectPenaltiesInLine]

    fieldsets = (
        (None,
         {'fields': ('title', 'image')}),
        ('Details Projet',
         {'fields': ('company', 'amount', 'external_code',
                     'delivery_date'
                     )}),

        ('Coordonées',
         {'fields': ('address', 'city', 'zip_code', 'country')}),
        ('Logos',
         {'fields': ('logo', 'logo2'
                     )}),
        ('Info supplémentaires',
         {'fields': ('workspace', 'report_templates', ('date_updated', 'date_created'))})
    )

    add_fieldsets = (
        ('Infos Projet', {
            'fields': ('title', 'image')}),
        ('Details Projet',
         {'fields': ('company', 'amount', 'external_code',
                     'delivery_date'
                     )}),
        ('Coordonées',
         {'fields': ('address', 'city', 'zip_code', 'country')}),
        ('Logos',
         {'fields': ('logo', 'logo2'
                     )}),
        ('Info supplémentaires',
         {'fields': ('workspace', 'report_templates')})
    )


class PhaseAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('project', 'name', 'type')
    list_filter = ()
    ordering = ("project", "name")

    fieldsets = (
        (None,
         {'fields': ('project',)}),
        ('Details Phase',
         {'fields': ('name', 'sub_name', 'is_locked',
                     'is_structural_work'
                     )}),
        ('Info supplémentaires',
         {'fields': ('is_available_on_purchaser_access', 'type', 'external_code', ('date_updated', 'date_created'))})
    )

    add_fieldsets = (
        ('Infos Projet', {
            'fields': ('project', 'image')}),
        ('Details Phase',
         {'fields': ('name', 'sub_name', 'is_locked',
                     'is_structural_work'
                     )}),
        ('Info supplémentaires',
         {'fields': ('is_available_on_purchaser_access', 'type', 'external_code')})
    )


class PlanAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('project', 'phase', 'general_plan_name', 'provider')
    list_filter = ()
    ordering = ("project", "phase")

    fieldsets = (
        (None,
         {'fields': ('project', 'phase', 'lot', 'general_plan_name')}),
        ('Details Plan',
         {'fields': ('provider', 'number', 'plan_type',
                     'index', 'drawing_src', 'delivery_date'
                     )}),
        ('Info localisation',
         {'fields': ('floor', 'building', 'zone_type', 'zone_category', 'lodgement_type')}),
        ('Info supplémentaires',
         {'fields': ('external_code', 'update_user', 'create_user', ('date_updated', 'date_created'))})
    )

    add_fieldsets = (
        ('Infos Projet', {
            'fields': ('project', 'phase', 'lot', 'general_plan_name')}),
        ('Details Plan',
         {'fields': ('provider', 'number', 'plan_type',
                     'index', 'drawing_src', 'delivery_date'
                     )}),
        ('Info localisation',
         {'fields': ('floor', 'building', 'zone_type', 'zone_category', 'lodgement_type')}),
        ('Info supplémentaires',
         {'fields': ('external_code', 'update_user', 'create_user')})
    )


class LotAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('phase', 'name', 'is_valided', 'is_completed')
    list_filter = ()
    ordering = ("phase", "name")
    
    inlines = [LotPenaltisInLine]

    fieldsets = (
        (None,
         {'fields': ('phase', 'name', 'is_valided')}),
        ('Details Lot',
         {'fields': ('holder_company', 'type_lot', 'amount', 'date_finale_commit_pv',
                     'last_transmitted_request_date'
                     )}),
        ('Info Pénalitées',
         {'fields': ('compensation_fee_paid', 'compensation_fee',)}),
        ('Info supplémentaires',
         {'fields': ('document', 'is_amendment', 'is_archived', 'is_completed', 'external_code', 'update_user_id', 'create_user_id', ('date_updated', 'date_created'))})
    )

    add_fieldsets = (
        ('Infos Projet', {
            'fields': ('phase', 'name')}),
        ('Details Lot',
         {'fields': ('holder_company', 'amount', 'date_finale_commit_pv',
                     'last_transmitted_request_date'
                     )}),
        ('Info Pénalitées',
         {'fields': ('penalties', 'compensation_fee_paid', 'compensation_fee')}),
        ('Info supplémentaires',
         {'fields': ('is_archived', 'is_completed', 'external_code', 'update_user_id', 'create_user_id')})
    )


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('user', 'name', 'priority', 'status')
    list_filter = ()
    ordering = ("user", "priority")

    fieldsets = (
        (None,
         {'fields': ('user', 'name', 'description', 'project', ('phase', 'lot'))}),
        ('Details Tâche',
         {'fields': ('priority', 'assigned_user', 'status',
                     )}),
        ('Photo',
         {'fields': ('photo',)}),
        ('Info supplémentaires',
         {'fields': ('is_archived', 'is_completed', 'date_completed', 'updated_user', ('date_updated', 'date_created'))})
    )

    add_fieldsets = (
        ('Infos Projet', {
            'fields': ('user', 'name', 'description', 'project', ('phase', 'lot'))}),
        ('Details Tâche',
         {'fields': ('priority', 'assigned_user', 'status',
                     )}),
        ('Photo',
         {'fields': ('photo',)}),
        ('Info supplémentaires',
         {'fields': ('is_archived', 'is_completed', 'date_completed', 'updated_user')})
    )


class FinancialStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('lot', 'number', 'amount')
    list_filter = ()
    ordering = ("lot", "number")

    fieldsets = (
        (None,
         {'fields': ('lot', 'number', 'month_financial_status')}),
        ('Details Situation',
         {'fields': ('amount', 'external_code', ('update_user_id', 'date_updated'),
                     ('create_user_id', 'date_created')
                     )}),
        ('Info supplémentaires',
         {'fields': (('is_recieved', 'is_classed', 'is_dispatched', 'is_valided_moe', 'is_broadcasted_architect'),)})
    )

    add_fieldsets = (
        ('Infos Situation', {
            'fields': ('lot', 'number', 'month_financial_status')}),
        ('Details Situation',
         {'fields': ('amount', 'external_code'
                     )}),
        ('Info supplémentaires',
         {'fields': (('is_recieved', 'is_classed', 'is_dispatched', 'is_valided_moe', 'is_broadcasted_architect'),)})
    )


moe_site.register(Phase, PhaseAdmin)
moe_site.register(Plan, PlanAdmin)
moe_site.register(Project, ProjectAdmin)
moe_site.register(Task, TaskAdmin)
moe_site.register(Lot, LotAdmin)
moe_site.register(TypeLot)
moe_site.register(FinancialStatus, FinancialStatusAdmin)
moe_site.register(LotPenalty)
moe_site.register(ProjectPenalty)
moe_site.register(PenaltyType)
# Register your models here.
