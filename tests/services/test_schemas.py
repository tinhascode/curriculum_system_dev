import pytest
from pydantic import ValidationError

from app.schemas.resume import Education, Experience, Resume


def test_resume_valid_minimal() -> None:
    resume = Resume(
        nome="João da Silva",
        cargo="Engenheiro de Software",
        email="joao@example.com",
        telefone="(11) 99999-9999",
    )
    assert resume.nome == "João da Silva"
    assert resume.cidade == ""
    assert resume.experiencias == []
    assert resume.formacao == []


def test_resume_invalid_email() -> None:
    with pytest.raises(ValidationError):
        Resume(
            nome="João da Silva",
            cargo="Engenheiro de Software",
            email="email-invalido",
            telefone="(11) 99999-9999",
        )


def test_resume_field_max_length() -> None:
    # nome max_length is 120
    with pytest.raises(ValidationError):
        Resume(
            nome="A" * 121,
            cargo="Engenheiro",
            email="joao@example.com",
            telefone="123",
        )


def test_resume_list_max_length() -> None:
    # habilidades max is 40
    with pytest.raises(ValidationError):
        Resume(
            nome="João",
            cargo="Engenheiro",
            email="joao@example.com",
            telefone="123",
            habilidades=[f"Skill {i}" for i in range(41)],
        )


def test_experience_limits() -> None:
    with pytest.raises(ValidationError):
        Experience(
            cargo="Dev",
            empresa="Empresa",
            periodo="2020",
            realizacoes=[f"Realizacao {i}" for i in range(11)],  # max 10
        )


def test_education_valid() -> None:
    edu = Education(
        curso="Engenharia de Software",
        instituicao="Universidade Federal",
        periodo="2018 - 2022",
    )
    assert edu.curso == "Engenharia de Software"
