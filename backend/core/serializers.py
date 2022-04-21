from rest_framework import serializers
from .models.models_clientes import Dossie
from .models.models_params import ParamsUser
from .models.models_log_actions import LogActions


class DossieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossie
        fields = "__all__"


class ParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParamsUser
        fields = "__all__"


class LogsActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogActions
        fields = "__all__"
