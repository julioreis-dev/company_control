from django.db import models
from ..models import *


class ParamsUser(models.Model):
    project = models.CharField(max_length=200, verbose_name="Nome do projeto")
    description = models.TextField(verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True)
    dossie = models.ForeignKey(Dossie, on_delete=models.CASCADE, related_name='dossie')
    def __str__(self):
        return f"{self.project}"

    class Meta:
        """
        Classe para ordenar e contextualizar o admin
        """
        # ordering = ('-date_insc',)
        verbose_name = 'Parametro'
        verbose_name_plural = 'Parametros'
