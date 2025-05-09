from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', include('produtos.urls')),  # aqui estamos incluindo as URLs do app 'produtos'
]

