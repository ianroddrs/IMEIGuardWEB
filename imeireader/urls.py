from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resultado/', views.resultado, name='resultado'),
    path('historico/', views.historico, name='historico'),
    path('login/', views.loginView, name='login'),
    path('logout', views.exit, name='exit'),
]