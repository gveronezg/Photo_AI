# importando o módulo de urls do django
from django.urls import path
# importando as views do projeto
from . import views

urlpatterns = [
    # path('') -> caminho vazio | views.home -> função que será chamada | name='home' -> nome da rota
    path('', views.home, name='home'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/<str:id_projeto>/', views.detalhes_projeto, name='detalhes_projeto')
]