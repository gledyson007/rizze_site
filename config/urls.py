from django.contrib import admin
from django.urls import path
from core.views import index # Importando a nossa view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), # Rota principal apontando para a view 'index'
]