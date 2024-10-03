from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_depense, name='ajouter_depense'),
    path('depenses/', views.lister_depenses, name='lister_depenses'),
    path('inscription/', views.register, name='register'),
]
