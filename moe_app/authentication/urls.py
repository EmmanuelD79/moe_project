from .views import ContactViewSet, LoginView, MyTokenObtainPairView, SignupView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path



router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
urlpatterns = router.urls

urlpatterns += [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view({'post': 'post'}), name='login'),
    path('register/', SignupView.as_view({'post': 'create'}), name='register'),
]

