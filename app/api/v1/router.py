from fastapi import APIRouter

from app.api.v1.catalog import router as catalog_router
from app.api.v1.resumes import router as resumes_router

api_v1_router = APIRouter()

api_v1_router.include_router(resumes_router)
api_v1_router.include_router(catalog_router)
