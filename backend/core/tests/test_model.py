import json
import pytest
from django.urls import reverse
from ..models.models_clientes import Dossie
import datetime
from ..models.models_params import ParamsUser

# pytest --cov=.

dossie_url = reverse("dossieview-list")
pytestmark = pytest.mark.django_db


def test_zero_clients_return_empty_list(client) -> None:
    response = client.get(dossie_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_client_exist_should_return_succeed(client) -> None:
    test_client = Dossie.objects.create(
        name="Firmino",
        address="Rua dos inválidos",
        email="firma@gmail.com",
        tel1="21985632147",
        tel2="21985632148",
    )
    response = client.get(dossie_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content["name"] == test_client.name
    assert response_content["address"] == test_client.address
    assert response_content["email"] == test_client.email
    assert response_content["tel1"] == test_client.tel1
    assert response_content["tel2"] == test_client.tel2


def test_create_client_should_return_succes(client) -> None:
    data_name = {
        "name": "Firmino",
        "address": "Rua dos invalidos",
        "email": "firma@gmail.com",
        "tel1": "21985632147",
        "tel2": "21985632148",
    }
    response = client.post(path=dossie_url, data=data_name)
    assert response.status_code == 201
    response_content = response.json()
    assert response_content["name"] == data_name["name"]
    assert response_content["address"] == data_name['address']
    assert response_content["email"] == data_name['email']
    assert response_content["tel1"] == data_name['tel1']
    assert response_content["tel2"] == data_name['tel2']


def test_one_client_exist_with_wrong_email_pattern_should_return_fail(client) -> None:
    Dossie.objects.create(
        name="Firmino",
        address="Rua dos inválidos",
        email="firma2gmail.com",
        tel1="21985632147",
        tel2="21985632148",
    )
    response = client.post(dossie_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "email": ["Este campo é obrigatório."],
        "name": ["Este campo é obrigatório."],
        "tel1": ["Este campo é obrigatório."],
    }


def test_register_only_one_argument_name_should_return_fail(client) -> None:
    Dossie.objects.create(name="Firmino")
    response = client.post(path=dossie_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "email": ["Este campo é obrigatório."],
        "name": ["Este campo é obrigatório."],
        "tel1": ["Este campo é obrigatório."],
    }


def test_register_only_one_argument_email_should_return_fail(client) -> None:
    Dossie.objects.create(email="firma@gmail.com")
    response = client.post(path=dossie_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "email": ["Este campo é obrigatório."],
        "name": ["Este campo é obrigatório."],
        "tel1": ["Este campo é obrigatório."],
    }


def test_register_only_one_argument_tel1_should_return_fail(client) -> None:
    Dossie.objects.create(tel1="21985632148")
    response = client.post(path=dossie_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "email": ["Este campo é obrigatório."],
        "name": ["Este campo é obrigatório."],
        "tel1": ["Este campo é obrigatório."],
    }


def test_one_client_exist_and_has_parms_should_return_succeed(client) -> None:
    test_client = Dossie.objects.create(
        name="Firmino",
        address="Rua dos inválidos",
        email="firma@gmail.com",
        tel1="21985632147",
        tel2="21985632148",
    )
    response = client.get(dossie_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content["name"] == test_client.name
    assert response_content["address"] == test_client.address
    assert response_content["email"] == test_client.email
    assert response_content["tel1"] == test_client.tel1
    assert response_content["tel2"] == test_client.tel2
