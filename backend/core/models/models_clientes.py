from ..models import *
from django.db import models
import datetime


class Dossie(models.Model):
    """
    Classe model para cadastro de novos clientes
    """

    name = models.CharField(max_length=200, verbose_name="nome")
    birthday = models.DateField(
        default=datetime.date.today, verbose_name="Nascimento", editable=True,
    )
    address = models.CharField(
        max_length=250, verbose_name="Endereço", null=True, blank=True
    )
    state = models.IntegerField(
        choices=CITIES, default=1, verbose_name="Estado"
    )
    email = models.EmailField(max_length=200, verbose_name="Email", unique=True)
    tel1 = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="Telefone (1)",
        help_text="Telefone 1 do cliente",
    )
    tel2 = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        unique=True,
        verbose_name="Telefone (2)",
        help_text="Telefone 2 do cliente",
    )
    insta = models.CharField(max_length=150, blank=True, verbose_name="Instagram")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
