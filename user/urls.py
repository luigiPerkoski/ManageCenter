from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login', views.view_login, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.view_register, name = 'register'),
]
