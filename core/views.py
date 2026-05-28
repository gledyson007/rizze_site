from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ConfigurracaoSite, Servico

def index(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    configuracao = ConfigurracaoSite.objects.first()

    servicos = Servico.objects.filter(ativo=True)

    context = {
        'config': configuracao,
        'servicos': servicos,
    }

    return render(request, 'index.html', context)
