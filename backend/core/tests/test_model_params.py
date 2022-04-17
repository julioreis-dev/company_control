import json
import pytest
from django.urls import reverse
import datetime
from ..models.models_clientes import Dossie
from ..models.models_params import ParamsUser


dossie_url = reverse("paramsview-list")
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
    response = client.get(dossie_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content["project"] == params_client.project
    assert response_content["description"] == params_client.description
    assert response_content["dossie"] == params_client.id
