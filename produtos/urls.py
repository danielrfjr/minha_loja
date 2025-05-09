from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'), # correção foi mudar views.cadastrar_produtos para views.cadastrar_produto, pois a função foi definida assim no views.
    path('listar/', views.listar_produto, name='listar_produto'),
]
