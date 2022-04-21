from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models.models_clientes import Dossie
from .models.models_params import ParamsUser
from .models.models_log_actions import LogActions
from .serializers import DossieSerializer, ParamsSerializer, LogsActionsSerializer


class DossieViewSet(viewsets.ModelViewSet):
    queryset = Dossie.objects.all()
    serializer_class = DossieSerializer


class ParamsViewsSet(viewsets.ModelViewSet):
    queryset = ParamsUser.objects.all()
    serializer_class = ParamsSerializer


class LogsActionsViewsSet(viewsets.ModelViewSet):
    queryset = LogActions.objects.all()
    serializer_class = LogsActionsSerializer
