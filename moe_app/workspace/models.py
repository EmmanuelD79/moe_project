from django.db import models
from authentication.models import DateTimeInfo, User
from assets.InfoBase import DateTimeInfo, Owner
from django.conf import settings

class Workspace(DateTimeInfo, Owner):
    name = models.CharField("Nom du workspace", max_length=256, blank=False)
    description = models.CharField("Description", max_length=1000, blank=False)
    state = models.CharField("Etat", max_length=20)
    kind = models.CharField("Type", max_length=20)

    class Meta:
        verbose_name = "Espace de travail"
        verbose_name_plural = "Espaces de travail"
        ordering = ('name',)

    def __str__(self):
        return f"{self.name} "


class Team(DateTimeInfo):
    name = models.CharField("Nom de l'équipe", max_length=256, blank=False)
    permission = models.CharField("permision", max_length=256, blank=True)
    workspace = models.ForeignKey(Workspace, verbose_name="Workspace", blank=False, on_delete=models.PROTECT)
    members = models.ManyToManyField(User, through='UserTeam', through_fields=('team', 'user'))
    
    class Meta:
        verbose_name = "Equipe"
        ordering = ('name',)
    
    def __str__(self):
        return f"{self.name}"

class UserTeam(models.Model):
    team = models.ForeignKey(Team, verbose_name="Equipe", on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name="Utilisateur", on_delete=models.CASCADE)
    date_joined_team = models.DateTimeField("Intégré(e) le", auto_now_add=True)
    status = models.CharField("Etat", max_length=50, blank=True)
    
    class Meta:
        unique_together = ('team', 'user')
        verbose_name = "Equipe-utilisateur"
        verbose_name_plural = "Equipes-Utilisateurs"

    def __str__(self):
        return f"{self.team} -> {self.user} "