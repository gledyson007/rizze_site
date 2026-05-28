from django.shortcuts import render
from .models import ConfigurracaoSite, Servico

def index(request):
    configuracao = ConfigurracaoSite.objects.first()

    servicos = Servico.objects.filter(ativo=True)

    context = {
        'config': configuracao,
        'servicos': servicos,
    }

    return render(request, 'index.html', context)
