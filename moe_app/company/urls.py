from .views import CompanyViewSet, CompanyCategoryViewSet
from rest_framework.routers import DefaultRouter


company_router = DefaultRouter()
company_router.register(r'companies', CompanyViewSet, basename='company')
urlpatterns = company_router.urls

company_category_router = DefaultRouter()
company_category_router.register(r'companycategories', CompanyCategoryViewSet, basename='company')
urlpatterns += company_category_router.urls
