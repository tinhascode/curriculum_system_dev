from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.catalog import router as catalog_router
from app.api.v1.router import api_v1_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

if settings.ALLOWED_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_v1_router, prefix=settings.API_V1_STR)
app.include_router(catalog_router, prefix="/api")


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok", "version": settings.VERSION}
