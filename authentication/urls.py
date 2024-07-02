from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('google/', views.GoogleLogin.as_view(), name="google_login"),
    path('google-signup/', views.GoogleSignUpView.as_view(), name="google_signup")
]