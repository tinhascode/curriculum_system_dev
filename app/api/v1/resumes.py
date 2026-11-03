from fastapi import APIRouter, HTTPException, Query, Response

from app.schemas.resume import Resume
from app.services.render import render_html

router = APIRouter(prefix="/resumes", tags=["Currículos"])


@router.post(
    "/preview",
    response_class=Response,
    summary="Renderizar pré-visualização HTML do currículo",
    responses={
        200: {
            "content": {"text/html": {}},
            "description": "HTML do currículo renderizado com Jinja2.",
        },
        400: {"description": "Template inválido."},
        422: {"description": "Erro de validação nos campos do currículo."},
    },
)
def preview_resume(
    resume: Resume,
    template: str = Query(
        default="classico",
        description="Identificador do template (ex: classico)",
    ),
) -> Response:
    try:
        html_content = render_html(
            resume=resume,
            template=template,
            inline_styles=True,
        )
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err)) from err

    return Response(content=html_content, media_type="text/html")
