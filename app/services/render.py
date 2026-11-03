from pathlib import Path

from jinja2 import Environment, FileSystemLoader, TemplateNotFound, select_autoescape

from app.schemas.resume import Resume

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_DIR)),
    autoescape=select_autoescape(["html", "xml"]),
)

SUPPORTED_TEMPLATES = {"classico"}


def get_available_templates() -> list[str]:
    return sorted(
        [
            d.name
            for d in TEMPLATES_DIR.iterdir()
            if d.is_dir() and (d / "resume.html").exists()
        ]
    )


def render_html(
    resume: Resume, template: str = "classico", inline_styles: bool = True
) -> str:
    template_name = template.lower().strip()
    template_path = f"{template_name}/resume.html"

    try:
        jinja_template = env.get_template(template_path)
    except TemplateNotFound as err:
        available = get_available_templates()
        raise ValueError(
            f"Template '{template}' não encontrado. Disponíveis: {available}"
        ) from err

    inline_css = ""
    if inline_styles:
        css_file = TEMPLATES_DIR / template_name / "style.css"
        if css_file.exists():
            inline_css = css_file.read_text(encoding="utf-8")

    return jinja_template.render(
        r=resume,
        inline_css=inline_css,
    )
