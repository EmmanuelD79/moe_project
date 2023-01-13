from django.contrib import admin
from authentication.admin import moe_site
from workspace.models import Workspace, Team, UserTeam


moe_site.register(Workspace)
moe_site.register(Team)
moe_site.register(UserTeam)
# Register your models here.
