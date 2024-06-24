from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resultado/', views.resultado, name='resultado'),
    path('result/', views.resultadoGET, name='result'),
    path('rec/', views.recuperacao, name='rec'),
    path('historico/', views.historico, name='historico'),
    path('cad_user/', views.cad_user, name='cad_user'),
    path('password', views.changePassword, name='password'),
    path('login/', views.loginView, name='login'),
    path('logout', views.exit, name='exit'),
    path('download/apk/', views.download_apk, name='download_apk'),
]