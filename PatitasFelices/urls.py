# PatitasFelices/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', views.home, name='home'),
    path('tienda/', views.tienda, name='tienda'),
    path('registro/', views.registro, name='registro'),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('turno/', views.solicitar_turno, name='solicitar_turno'),
]



