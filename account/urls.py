from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, ActivationView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("activate/<str:email>/<str:activation_code>/", ActivationView.as_view(), name="activate"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh")
]