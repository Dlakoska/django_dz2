from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, reset_password, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('register/', UserCreateView.as_view(template_name="users/register.html"), name="register"),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),
    path('reset_password/', reset_password, name='reset_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
]