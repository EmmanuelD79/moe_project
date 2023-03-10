# Generated by Django 4.1.3 on 2023-01-12 16:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('workspace', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('name', models.CharField(max_length=256, verbose_name='Nom')),
                ('external_code', models.CharField(blank=True, max_length=256, verbose_name='Code externe')),
                ('compensation_fee_paid', models.FloatField(default=0, verbose_name='Pénalité payée')),
                ('compensation_fee', models.FloatField(default=0, verbose_name='Pénalité')),
                ('last_transmitted_request_date', models.DateField(verbose_name='Date de dernière demande')),
                ('date_finale_commit_pv', models.DateField(verbose_name='Date de dernier PV')),
                ('amount', models.FloatField(default=0, verbose_name='Montant')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Archivé')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Terminé')),
                ('is_valided', models.BooleanField(default=False, verbose_name='Validé par MOA')),
                ('is_amendment', models.BooleanField(default=False, verbose_name='Avenant')),
                ('document', models.FileField(blank=True, upload_to='document/', verbose_name='Document')),
                ('create_user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lot_create_user', to=settings.AUTH_USER_MODEL, verbose_name='Crée par')),
                ('holder_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.company', verbose_name='Gestionnaire du Lot')),
            ],
            options={
                'verbose_name': 'Lot',
                'ordering': ('phase', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='PenaltyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Titre')),
            ],
            options={
                'verbose_name': 'Type de pénalité',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('name', models.CharField(max_length=256, verbose_name='Nom')),
                ('sub_name', models.CharField(max_length=256, verbose_name='Sous-menu')),
                ('is_locked', models.BooleanField(default=False, verbose_name='Fermé')),
                ('is_structural_work', models.BooleanField(default=False, verbose_name='Travaux GO')),
                ('is_available_on_purchaser_access', models.BooleanField(default=False, verbose_name="Accès à l'acheteur")),
                ('type', models.CharField(max_length=256, verbose_name='Type')),
                ('external_code', models.CharField(blank=True, max_length=256, verbose_name='Code externe')),
            ],
            options={
                'verbose_name': 'Phase',
                'ordering': ('project', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Adresse')),
                ('city', models.CharField(blank=True, max_length=200, verbose_name='Ville')),
                ('zip_code', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Code postal')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Pays')),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project/images/', verbose_name='Image')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='project/logos/', verbose_name='1er logo')),
                ('logo2', models.ImageField(blank=True, null=True, upload_to='project/logos/', verbose_name='2ème logo')),
                ('amount', models.FloatField(default=0, verbose_name='Montant')),
                ('external_code', models.CharField(blank=True, max_length=256, verbose_name='Code externe')),
                ('delivery_date', models.DateField(blank=True, null=True, verbose_name='Date de livraison')),
                ('report_templates', models.CharField(blank=True, max_length=256, verbose_name='Modèle de rapport')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.company', verbose_name="Maitre d'ouvrage")),
            ],
            options={
                'verbose_name': 'Projet',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='TypeLot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Type de Lot',
                'verbose_name_plural': 'Types de Lot',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('name', models.CharField(max_length=256, verbose_name='Titre')),
                ('description', models.TextField(max_length=6000, verbose_name='Description')),
                ('priority', models.CharField(max_length=50, verbose_name='Priorité')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Terminé')),
                ('date_completed', models.DateTimeField(verbose_name='Terminé le')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Archivé')),
                ('photo', models.ImageField(upload_to='task/photos/', verbose_name='Photo')),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_assigned_user', to=settings.AUTH_USER_MODEL, verbose_name='Assigné(e) à la tâche')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.lot', verbose_name='Lot')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.phase', verbose_name='Phase')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project', verbose_name='Projet')),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_update_user', to=settings.AUTH_USER_MODEL, verbose_name='Mise à jour par')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_user', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Tâche',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ProjectPenalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('value', models.FloatField(default=0, verbose_name='Montant')),
                ('penalty_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_penalty_type', to='project.penaltytype', verbose_name='Type de pénalité')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_penalty', to='project.project', verbose_name='Projet')),
            ],
            options={
                'verbose_name': 'Pénalité du Projet',
                'verbose_name_plural': 'Pénalités du Projet',
                'unique_together': {('project', 'penalty_type')},
            },
        ),
        migrations.AddField(
            model_name='project',
            name='penalties',
            field=models.ManyToManyField(blank=True, through='project.ProjectPenalty', to='project.penaltytype'),
        ),
        migrations.AddField(
            model_name='project',
            name='workspace',
            field=models.ManyToManyField(blank=True, to='workspace.workspace'),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('general_plan_name', models.CharField(max_length=256, verbose_name='Nom du plan')),
                ('number', models.CharField(max_length=256, verbose_name='Numéro du plan')),
                ('plan_type', models.CharField(max_length=256, verbose_name='Type de plan')),
                ('floor', models.CharField(blank=True, max_length=256, verbose_name='Etage')),
                ('building', models.CharField(blank=True, max_length=256, verbose_name='Bâtiment')),
                ('zone_type', models.CharField(blank=True, max_length=256, verbose_name='Type de zone')),
                ('zone_category', models.CharField(blank=True, max_length=256, verbose_name='Catégorie de la zone')),
                ('lodgement_type', models.CharField(blank=True, max_length=256, verbose_name='Type de logement')),
                ('index', models.CharField(blank=True, max_length=256, verbose_name='Indice du plan')),
                ('drawing_src', models.FileField(upload_to='plans/', verbose_name='Fichier')),
                ('delivery_date', models.DateField(blank=True, verbose_name='Date de remise')),
                ('external_code', models.CharField(blank=True, max_length=256, verbose_name='Code externe')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='plan_create_user', to=settings.AUTH_USER_MODEL, verbose_name='Crée par')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.lot', verbose_name='Lot')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.phase', verbose_name='Phase')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.project', verbose_name='Projet')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.company', verbose_name='Créateur')),
                ('update_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='plan_update_user', to=settings.AUTH_USER_MODEL, verbose_name='Mis à jour par')),
            ],
            options={
                'verbose_name': 'Plan',
                'ordering': ('project', 'phase', 'lot'),
            },
        ),
        migrations.AddField(
            model_name='phase',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.project', verbose_name='Projet'),
        ),
        migrations.CreateModel(
            name='LotPenalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nombre de jours')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lot_project_penalty', to='project.lot', verbose_name='Lot')),
                ('project_penalty_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lot_project_penalty', to='project.projectpenalty', verbose_name='Pénalité')),
            ],
            options={
                'verbose_name': 'Pénalité du lot',
                'verbose_name_plural': 'Pénalités des lots',
                'unique_together': {('project_penalty_type', 'lot')},
            },
        ),
        migrations.AddField(
            model_name='lot',
            name='penalties',
            field=models.ManyToManyField(blank=True, related_name='lot_project_penalties', through='project.LotPenalty', to='project.projectpenalty'),
        ),
        migrations.AddField(
            model_name='lot',
            name='phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.phase', verbose_name='Phase'),
        ),
        migrations.AddField(
            model_name='lot',
            name='type_lot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lot_type_lot', to='project.typelot', verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='lot',
            name='update_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lot_update_user', to=settings.AUTH_USER_MODEL, verbose_name='Mise à jour par'),
        ),
        migrations.CreateModel(
            name='FinancialStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Mise à jour le')),
                ('number', models.PositiveIntegerField(blank=True, null=True, verbose_name='N° Situation')),
                ('external_code', models.CharField(blank=True, max_length=256, verbose_name='Code externe')),
                ('amount', models.FloatField(default=0, verbose_name='Montant')),
                ('month_financial_status', models.DateField(verbose_name='Mois')),
                ('is_recieved', models.BooleanField(default=False, verbose_name='reçu')),
                ('is_classed', models.BooleanField(default=False, verbose_name='Classé')),
                ('is_dispatched', models.BooleanField(default=False, verbose_name='Bordereau')),
                ('is_valided_moe', models.BooleanField(default=False, verbose_name='Validé par MOE')),
                ('is_broadcasted_architect', models.BooleanField(default=False, verbose_name="Diffusé à l'architecte")),
                ('create_user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='financial_status_create_user', to=settings.AUTH_USER_MODEL, verbose_name='Crée par')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lot_financial_status', to='project.lot', verbose_name='Lot')),
                ('update_user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='financial_status_update_user', to=settings.AUTH_USER_MODEL, verbose_name='Mise à jour par')),
            ],
            options={
                'verbose_name': 'Situation',
                'ordering': ('lot', 'pk'),
            },
        ),
    ]
