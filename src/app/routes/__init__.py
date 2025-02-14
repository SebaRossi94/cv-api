from fastapi.routing import APIRouter
from app.settings import settings
from .users import router as users_router

router = APIRouter()

@router.get("/health")
def read_root():
    return {"Hello": "World"}


@router.get("/settings")
def read_settings():
    return settings.model_dump()

router.include_router(users_router)