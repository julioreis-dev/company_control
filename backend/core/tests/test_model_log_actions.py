import json
import pytest
from django.urls import reverse
from ..models.models_log_actions import LogActions
from ..models.models_clientes import Dossie
from ..models.models_params import ParamsUser

logs_url = reverse("logsactionview-list")
pytestmark = pytest.mark.django_db


def test_one_logaction_should_return_succeed(client) -> None:
    test_client = Dossie.objects.create(
        name="Firmino",
        address="Rua dos inválidos",
        email="firma@gmail.com",
        tel1="21985632147",
        tel2="21985632148",
    )
    params_client = ParamsUser.objects.create(
        project="banco", description="projeto banco", dossie=test_client
    )
    test_logaction = LogActions.objects.create(
        name_project="imobiliaria",
        action_description="ajuste google",
        paramsuser=params_client,
    )
    response = client.get(path=logs_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content["name_project"] == test_logaction.name_project
    assert response_content["action_description"] == test_logaction.action_description
    assert response_content["paramsuser"] == test_logaction.id


def test_register_miss_name_project_in_logactions_fail(client) -> None:
    data_logactions = {"name_project": "imobiliaria"}
    response = client.post(path=logs_url, data=data_logactions)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "action_description": ["Este campo é obrigatório."],
        "paramsuser": ["Este campo é obrigatório."],
    }


def test_register_miss_action_description_in_logactions_fail(client) -> None:
    data_logactions = {"action_description": "imobiliaria"}
    response = client.post(path=logs_url, data=data_logactions)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name_project": ["Este campo é obrigatório."],
        "paramsuser": ["Este campo é obrigatório."],
    }
