from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('musicas', views.musicas, name='musicas'),
    path('sobre', views.sobre, name='sobre'),
]
