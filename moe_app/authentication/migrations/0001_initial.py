# Generated by Django 4.1.3 on 2023-01-12 16:31

import authentication.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')], verbose_name='Téléphone')),
                ('mobile', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')], verbose_name='Portable')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Adresse')),
                ('city', models.CharField(blank=True, max_length=200, verbose_name='Ville')),
                ('zip_code', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Code postal')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Pays')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Né(e) le')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='Poste')),
                ('url', models.URLField(blank=True, max_length=256, null=True, verbose_name='Url')),
                ('photo_original', models.ImageField(blank=True, null=True, upload_to='photo_profil/', verbose_name='Photo de profil')),
                ('time_zone_identifier', models.CharField(blank=True, max_length=10, verbose_name='UTC')),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=256, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=256, verbose_name='Nom')),
                ('is_guest', models.BooleanField(default=False, verbose_name='invité')),
                ('is_staff', models.BooleanField(default=True, verbose_name='utilisateur')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Administrateur')),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'ordering': ('email',),
            },
            managers=[
                ('objects', authentication.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
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
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Email')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Né(e) le')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='Poste')),
                ('url', models.URLField(blank=True, max_length=256, null=True, verbose_name='Url')),
                ('photo_original', models.ImageField(blank=True, null=True, upload_to='photo_profil/', verbose_name='Photo de profil')),
                ('time_zone_identifier', models.CharField(blank=True, max_length=10, verbose_name='UTC')),
                ('first_name', models.CharField(max_length=256, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=256, verbose_name='Nom')),
                ('sub_type', models.CharField(blank=True, max_length=100, verbose_name='type')),
                ('is_private', models.BooleanField(default=False, verbose_name='Privé')),
            ],
            options={
                'verbose_name': 'Contact',
                'ordering': ('pk',),
            },
        ),
    ]
