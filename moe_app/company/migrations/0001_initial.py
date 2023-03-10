# Generated by Django 4.1.3 on 2023-01-12 16:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Catégorie',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')], verbose_name='Téléphone')),
                ('mobile', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')], verbose_name='Portable')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Adresse')),
                ('city', models.CharField(blank=True, max_length=200, verbose_name='Ville')),
                ('zip_code', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Code postal')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Pays')),
                ('identification_code', models.CharField(max_length=14, verbose_name='siret')),
                ('identification_type', models.CharField(max_length=10, verbose_name='Forme juridique')),
                ('legal_name', models.CharField(max_length=100, verbose_name='Nom commercial')),
                ('status', models.CharField(blank=True, max_length=100, verbose_name='Status')),
                ('website', models.URLField(blank=True, max_length=256, verbose_name='Site')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.companycategory', verbose_name='Catégorie')),
                ('company_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='holding', to='company.company', verbose_name='Groupe')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Propriétaire')),
            ],
            options={
                'verbose_name': 'Société',
                'ordering': ('legal_name',),
            },
        ),
    ]
