from django.shortcuts import render
from rest_framework import viewsets
from .models.models_clientes import Dossie
from .serializers import DossieSerializer


class DossieViewSet(viewsets.ModelViewSet):
    queryset = Dossie.objects.all()
    serializer_class = DossieSerializer
