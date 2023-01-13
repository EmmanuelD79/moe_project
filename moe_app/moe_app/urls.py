from django.urls import path, include
from authentication.admin import moe_site


urlpatterns = [
    path('moe/', moe_site.urls),
    path('api/', include('authentication.urls')),
    path('api/', include('company.urls')),
]
