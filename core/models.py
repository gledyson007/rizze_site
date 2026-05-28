from django.db import models

class ConfigurracaoSite(models.Model):
    titulo_principal = models.CharField(max_length=255, default="Especialistas em Ar-Condicionado em Petrópolis")
    subtitulo = models.TextField(default="Instalação, manutenção e higienização com garantia de qualidade.")

    numero_whatsapp = models.CharField(max_length=20, default="5524992116050", help_text="Apenas números, com DDI e DDD.")
    email_contato = models.EmailField(default="refrigeracaopetropolis@gmail.com")
    link_instagram = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configurações do Site"

    def __str__(self):
        return "Configuraçãoes Gerais do Site"
    
class Servico(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    # Para o ícone, podemos usar o emoji que ele gostou ou subir uma imagem depois
    icone_emoji = models.CharField(max_length=10, default="❄️", help_text="Coloque um emoji para representar o serviço")
    ativo = models.BooleanField(default=True)
    ordem_exibicao = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['ordem_exibicao']

    def __str__(self):
        return self.titulo