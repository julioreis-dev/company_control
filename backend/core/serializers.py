from rest_framework import serializers
from .models.models_clientes import Dossie
from .models.models_params import ParamsUser


class DossieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossie
        fields = "__all__"


class ParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParamsUser
        fields = "__all__"