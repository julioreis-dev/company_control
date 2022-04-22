import json
import pytest
from django.urls import reverse
from ..models.models_clientes import Dossie
from ..models.models_params import ParamsUser

params_url = reverse("paramsview-list")
pytestmark = pytest.mark.django_db


def test_one_client_has_params_should_return_succeed(client) -> None:
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
    response = client.get(params_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content["project"] == params_client.project
    assert response_content["description"] == params_client.description
    assert response_content["dossie"] == params_client.id


def test_register_miss_project_params_should_fail(client) -> None:
    data_params = {"description": "project register user"}
    response = client.post(path=params_url, data=data_params)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "dossie": ["Este campo é obrigatório."],
        "project": ["Este campo é obrigatório."],
    }


def test_register_miss_description_should_fail(client) -> None:
    data_params = {"project": "project register user"}
    response = client.post(path=params_url, data=data_params)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "dossie": ["Este campo é obrigatório."],
        "description": ["Este campo é obrigatório."],
    }
