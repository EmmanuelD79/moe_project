from django.db import models
from authentication.models import User
from assets.InfoBase import DateTimeInfo, AddressInfo
from workspace.models import Workspace
from company.models import Company


class PenaltyType(models.Model):
    name = models.CharField("Titre", max_length=256, blank=False)

    class Meta:
        verbose_name = "Type de pénalité"
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"


class Project(DateTimeInfo, AddressInfo):
    workspace = models.ManyToManyField(Workspace, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, verbose_name="Maitre d'ouvrage", blank=False)
    title = models.CharField(max_length=256, blank=False)
    image = models.ImageField(
        upload_to='project/images/', verbose_name="Image", blank=True, null=True)
    logo = models.ImageField(upload_to='project/logos/',
                             verbose_name="1er logo", blank=True, null=True)
    logo2 = models.ImageField(
        upload_to='project/logos/', verbose_name="2ème logo", blank=True, null=True)
    amount = models.FloatField("Montant", default=0)
    external_code = models.CharField(
        "Code externe", max_length=256, blank=True)
    delivery_date = models.DateField(
        "Date de livraison", blank=True, null=True)
    report_templates = models.CharField(
        "Modèle de rapport", blank=True, max_length=256)
    penalties = models.ManyToManyField(
        PenaltyType, through='ProjectPenalty', through_fields=('project', 'penalty_type'), blank=True)

    class Meta:
        verbose_name = "Projet"
        ordering = ('pk',)

    def __str__(self):
        return f"{self.title} | {self.amount}"


class Phase(DateTimeInfo):
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, verbose_name="Projet", blank=False)
    name = models.CharField("Nom", max_length=256, blank=False)
    sub_name = models.CharField("Sous-menu", max_length=256, blank=False)
    is_locked = models.BooleanField(default=False, verbose_name="Fermé")
    is_structural_work = models.BooleanField(
        default=False, verbose_name="Travaux GO")
    is_available_on_purchaser_access = models.BooleanField(
        default=False, verbose_name="Accès à l'acheteur")
    type = models.CharField("Type", max_length=256, blank=False)
    external_code = models.CharField(
        "Code externe", max_length=256, blank=True)

    class Meta:
        verbose_name = "Phase"
        ordering = ('project', 'name')

    def __str__(self):
        return f"{self.project} | {self.name}"


class ProjectPenalty(DateTimeInfo):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                verbose_name="Projet", related_name='project_penalty')
    penalty_type = models.ForeignKey(PenaltyType, on_delete=models.CASCADE,
                                     verbose_name="Type de pénalité", related_name='project_penalty_type')
    value = models.FloatField("Montant", default=0)

    class Meta:
        unique_together = ('project', 'penalty_type')
        verbose_name = "Pénalité du Projet"
        verbose_name_plural = "Pénalités du Projet"

    def __str__(self):
        return f"{self.project} -> {self.penalty_type} "


class TypeLot(models.Model):
    name = models.CharField("Nom", max_length=256, blank=False)

    class Meta:
        verbose_name = "Type de Lot"
        verbose_name_plural = "Types de Lot"
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"


class Lot(DateTimeInfo):
    phase = models.ForeignKey(
        Phase, on_delete=models.PROTECT, verbose_name="Phase")
    name = models.CharField("Nom", max_length=256, blank=False)
    external_code = models.CharField(
        "Code externe", max_length=256, blank=True)
    compensation_fee_paid = models.FloatField("Pénalité payée", default=0)
    compensation_fee = models.FloatField("Pénalité", default=0)
    last_transmitted_request_date = models.DateField(
        "Date de dernière demande")
    update_user_id = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Mise à jour par", related_name='lot_update_user')
    create_user_id = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Crée par", related_name='lot_create_user')
    type_lot = models.ForeignKey(
        TypeLot, on_delete=models.PROTECT, verbose_name="Type", related_name='lot_type_lot')
    date_finale_commit_pv = models.DateField("Date de dernier PV")
    amount = models.FloatField("Montant", default=0)
    holder_company = models.ForeignKey(
        Company, on_delete=models.PROTECT, verbose_name="Gestionnaire du Lot")
    is_archived = models.BooleanField(default=False, verbose_name="Archivé")
    is_completed = models.BooleanField(default=False, verbose_name="Terminé")
    is_valided = models.BooleanField(
        default=False, verbose_name="Validé par MOA")
    is_amendment = models.BooleanField(default=False, verbose_name="Avenant")
    document = models.FileField(
        verbose_name="Document", upload_to='document/', blank=True)
    penalties = models.ManyToManyField(
        ProjectPenalty, related_name="lot_project_penalties", through='LotPenalty', blank=True)

    class Meta:
        verbose_name = "Lot"
        ordering = ('phase', 'pk')

    def __str__(self):
        return f"{self.phase} | {self.name}"


class LotPenalty(DateTimeInfo):
    project_penalty_type = models.ForeignKey(
        ProjectPenalty, on_delete=models.CASCADE, verbose_name="Pénalité", related_name='lot_project_penalty')
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE,
                            verbose_name="Lot", related_name='lot_project_penalty')
    value = models.PositiveIntegerField("Nombre de jours", blank=True, null=True)

    class Meta:
        unique_together = ('project_penalty_type', 'lot')
        verbose_name = "Pénalité du lot"
        verbose_name_plural = "Pénalités des lots"

    def __str__(self):
        return f"{self.project_penalty_type.project} -> {self.lot.name}"


class FinancialStatus(DateTimeInfo):
    lot = models.ForeignKey(Lot, on_delete=models.PROTECT,
                            verbose_name="Lot", related_name='lot_financial_status')
    update_user_id = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Mise à jour par", related_name='financial_status_update_user')
    create_user_id = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Crée par", related_name='financial_status_create_user')
    number = models.PositiveIntegerField(
        "N° Situation", blank=True, null=True)
    external_code = models.CharField(
        "Code externe", max_length=256, blank=True)
    amount = models.FloatField("Montant", default=0)
    month_financial_status = models.DateField("Mois")
    is_recieved = models.BooleanField(default=False, verbose_name="reçu")
    is_classed = models.BooleanField(default=False, verbose_name="Classé")
    is_dispatched = models.BooleanField(
        default=False, verbose_name="Bordereau")
    is_valided_moe = models.BooleanField(
        default=False, verbose_name="Validé par MOE")
    is_broadcasted_architect = models.BooleanField(
        default=False, verbose_name="Diffusé à l'architecte")

    class Meta:
        verbose_name = "Situation"
        ordering = ('lot', 'pk')

    def __str__(self):
        return f"{self.lot.name} | {self.month_financial_status.month} / {self.month_financial_status.year} "


class Plan(DateTimeInfo):
    provider = models.ForeignKey(
        Company, on_delete=models.PROTECT, verbose_name="Créateur", blank=False)
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, verbose_name="Projet", blank=False)
    lot = models.ForeignKey(Lot, on_delete=models.PROTECT,
                            verbose_name="Lot", blank=False)
    phase = models.ForeignKey(
        Phase, on_delete=models.PROTECT, verbose_name="Phase")
    general_plan_name = models.CharField(
        "Nom du plan", max_length=256, blank=False)
    number = models.CharField("Numéro du plan", max_length=256, blank=False)
    plan_type = models.CharField("Type de plan", max_length=256, blank=False)
    floor = models.CharField("Etage", max_length=256, blank=True)
    building = models.CharField("Bâtiment", max_length=256, blank=True)
    zone_type = models.CharField("Type de zone", max_length=256, blank=True)
    zone_category = models.CharField(
        "Catégorie de la zone", max_length=256, blank=True)
    lodgement_type = models.CharField(
        "Type de logement", max_length=256, blank=True)
    index = models.CharField("Indice du plan", max_length=256, blank=True)
    drawing_src = models.FileField(
        verbose_name="Fichier", upload_to='plans/', blank=False)
    delivery_date = models.DateField("Date de remise", blank=True)
    external_code = models.CharField(
        "Code externe", max_length=256, blank=True)
    update_user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Mis à jour par", related_name='plan_update_user', blank=True)
    create_user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Crée par", related_name='plan_create_user', blank=False)

    class Meta:
        verbose_name = "Plan"
        ordering = ('project', 'phase', 'lot')

    def __str__(self):
        return f"{self.project.title} | {self.general_plan_name} | {self.provider.legal_name}"


class Task(DateTimeInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Utilisateur", related_name='task_user')
    name = models.CharField("Titre", max_length=256, blank=False)
    description = models.TextField("Description", max_length=6000)
    priority = models.CharField("Priorité", max_length=50)
    assigned_user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Assigné(e) à la tâche", related_name='task_assigned_user')
    status = models.CharField("Status", max_length=100)
    is_completed = models.BooleanField(default=False, verbose_name="Terminé")
    date_completed = models.DateTimeField("Terminé le")
    is_archived = models.BooleanField(default=False, verbose_name="Archivé")
    photo = models.ImageField(upload_to='task/photos/', verbose_name="Photo")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name="Projet")
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, verbose_name="Lot")
    phase = models.ForeignKey(
        Phase, on_delete=models.CASCADE, verbose_name="Phase")
    updated_user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Mise à jour par", related_name='task_update_user')

    class Meta:
        verbose_name = "Tâche"
        ordering = ('pk',)

    def __str__(self):
        return f"{self.name} | {self.priority} | {self.project.title}"
