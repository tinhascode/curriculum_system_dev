import json
from pathlib import Path
from typing import Any

from fastapi import APIRouter

from app.services.render import get_available_templates

router = APIRouter(tags=["Catálogo"])

AREAS_FILE = Path(__file__).resolve().parent.parent.parent / "data" / "areas.json"


@router.get("/areas", summary="Listar áreas profissionais e modelos iniciais")
def list_areas() -> list[dict[str, Any]]:
    if not AREAS_FILE.exists():
        return []
    with AREAS_FILE.open("r", encoding="utf-8") as f:
        areas: list[dict[str, Any]] = json.load(f)
    return areas


@router.get("/templates", summary="Listar templates disponíveis")
def list_templates() -> list[dict[str, str]]:
    templates = get_available_templates()
    templates_metadata = {
        "classico": {
            "id": "classico",
            "nome": "Clássico",
            "descricao": (
                "Layout em coluna única tradicional, altamente recomendado "
                "para compatibilidade ATS máxima."
            ),
        },
        "moderno": {
            "id": "moderno",
            "nome": "Moderno",
            "descricao": (
                "Visual limpo e contemporâneo com destaque sutil em cabeçalhos."
            ),
        },
        "compacto": {
            "id": "compacto",
            "nome": "Compacto",
            "descricao": (
                "Espaçamento otimizado para condensar histórico extenso "
                "em poucas páginas."
            ),
        },
    }

    return [
        templates_metadata.get(
            t,
            {
                "id": t,
                "nome": t.capitalize(),
                "descricao": f"Template {t}",
            },
        )
        for t in templates
    ]
