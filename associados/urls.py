from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_associado, name='cadastrar_associado'),
    path('lista/', views.lista_associados, name='lista_associados'),
]
