from django.db import models
from ..models import *


class LogActions(models.Model):
    name_project = models.CharField(max_length=200, verbose_name="Nome do projeto")
    action_description = models.TextField(verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True)
    paramsuser = models.ForeignKey(
        ParamsUser, on_delete=models.CASCADE, related_name="params"
    )

    def __str__(self):
        return f"{self.name_project}"

    class Meta:
        """
        Classe para ordenar e contextualizar o admin
        """

        verbose_name = "Correção"
        verbose_name_plural = "Correções"
