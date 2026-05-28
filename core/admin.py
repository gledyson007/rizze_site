from django.contrib import admin
from .models import ConfigurracaoSite, Servico

@admin.register(ConfigurracaoSite)
class ConfigurracaoSiteAdmin(admin.ModelAdmin):
    # Garante que ninguém adicione uma segunda "Configuração do Site", apenas edite a existente
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'icone_emoji', 'ativo', 'ordem_exibicao')
    list_editable = ('ativo', 'ordem_exibicao') # Permite mudar a ordem e ativar/desativar rápido