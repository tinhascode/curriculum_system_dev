import pytest

from app.schemas.resume import Education, Experience, Resume
from app.services.render import get_available_templates, render_html


@pytest.fixture
def sample_resume() -> Resume:
    return Resume(
        nome="Lucas Silva",
        cargo="Desenvolvedor Backend",
        email="lucas@exemplo.com",
        telefone="(11) 98765-4321",
        cidade="São Paulo, SP",
        link="https://github.com/lucas",
        resumo="Profissional experiente em Python e APIs.",
        experiencias=[
            Experience(
                cargo="Backend Engineer",
                empresa="Tech Co",
                periodo="2022 - Atual",
                realizacoes=["Construiu APIs", "Otimizou queries"],
            )
        ],
        formacao=[
            Education(
                curso="Ciência da Computação",
                instituicao="USP",
                periodo="2018 - 2022",
            )
        ],
        habilidades=["Python", "FastAPI", "Docker"],
        idiomas_certificacoes=["Inglês Avançado"],
    )


def test_available_templates() -> None:
    templates = get_available_templates()
    assert "classico" in templates


def test_render_html_contains_standard_sections(sample_resume: Resume) -> None:
    html = render_html(sample_resume, template="classico")

    assert "Resumo Profissional" in html
    assert "Experiência Profissional" in html
    assert "Formação Acadêmica" in html
    assert "Habilidades" in html
    assert "Idiomas e Certificações" in html

    assert "Lucas Silva" in html
    assert "Backend Engineer" in html
    assert "Tech Co" in html
    assert "Ciência da Computação" in html
    assert "Python • FastAPI • Docker" in html


def test_render_html_no_tables(sample_resume: Resume) -> None:
    html = render_html(sample_resume, template="classico")
    assert "<table" not in html.lower()
    assert "<td" not in html.lower()
    assert "<tr" not in html.lower()


def test_render_html_escapes_xss_injection() -> None:
    malicious_resume = Resume(
        nome="<script>alert('hack')</script>",
        cargo="Engenheiro & <img src=x onerror=alert(1)>",
        email="hacker@exemplo.com",
        telefone="123",
        resumo="<b>Tentativa</b> de injeção <iframe src='malicious.com'></iframe>",
        habilidades=["<svg onload=alert(1)>"],
    )

    html = render_html(malicious_resume, template="classico")

    assert "<script>" not in html
    assert "&lt;script&gt;alert(&#39;hack&#39;)&lt;/script&gt;" in html
    assert "<iframe" not in html
    assert "&lt;iframe" in html
    assert "<img" not in html
    assert "&lt;img" in html
    assert "<svg" not in html
    assert "&lt;svg" in html


def test_render_invalid_template(sample_resume: Resume) -> None:
    with pytest.raises(ValueError, match="não encontrado"):
        render_html(sample_resume, template="template_inexistente")
