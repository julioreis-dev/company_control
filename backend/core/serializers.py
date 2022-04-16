from rest_framework import serializers
from .models.models_clientes import Dossie


class DossieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossie
        fields = "__all__"
