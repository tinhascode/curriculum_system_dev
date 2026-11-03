from fastapi.testclient import TestClient


def test_preview_endpoint_success(client: TestClient) -> None:
    payload = {
        "nome": "Ana Souza",
        "cargo": "Product Manager",
        "email": "ana@exemplo.com",
        "telefone": "(11) 98888-7777",
        "cidade": "Campinas, SP",
        "link": "https://linkedin.com/in/anasouza",
        "resumo": "PM com foco em produtos digitais B2B.",
        "experiencias": [
            {
                "cargo": "Senior PM",
                "empresa": "TechCorp",
                "periodo": "2021 - Atual",
                "realizacoes": ["Lançou novo módulo", "Aumentou retenção em 20%"],
            }
        ],
        "formacao": [
            {
                "curso": "Administração",
                "instituicao": "Unicamp",
                "periodo": "2015 - 2019",
            }
        ],
        "habilidades": ["Scrum", "Product Discovery", "SQL"],
        "idiomas_certificacoes": ["Inglês Fluente"],
    }

    response = client.post("/api/v1/resumes/preview?template=classico", json=payload)
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    html = response.text
    assert "Ana Souza" in html
    assert "Product Manager" in html
    assert "Resumo Profissional" in html
    assert "Experiência Profissional" in html


def test_preview_endpoint_validation_error_422(client: TestClient) -> None:
    invalid_payload = {
        "cargo": "Desenvolvedor",
        "email": "invalido",
        "telefone": "123",
    }
    response = client.post("/api/v1/resumes/preview", json=invalid_payload)
    assert response.status_code == 422


def test_preview_endpoint_invalid_template_400(client: TestClient) -> None:
    valid_payload = {
        "nome": "Ana Souza",
        "cargo": "PM",
        "email": "ana@exemplo.com",
        "telefone": "(11) 98888-7777",
    }
    response = client.post(
        "/api/v1/resumes/preview?template=template_invalido", json=valid_payload
    )
    assert response.status_code == 400
    assert "Template 'template_invalido' não encontrado" in response.json()["detail"]


def test_get_areas_endpoint(client: TestClient) -> None:
    for route in ["/api/v1/areas", "/api/areas"]:
        response = client.get(route)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 4
        area_ids = [area["id"] for area in data]
        assert "tecnologia" in area_ids
        assert "dados" in area_ids
        assert "administrativo-financeiro" in area_ids
        assert "comercial-marketing" in area_ids


def test_get_templates_endpoint(client: TestClient) -> None:
    for route in ["/api/v1/templates", "/api/templates"]:
        response = client.get(route)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        template_ids = [t["id"] for t in data]
        assert "classico" in template_ids
