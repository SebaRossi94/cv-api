from fastapi.routing import APIRouter
from app.settings import settings
router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/settings")
def read_settings():
    return settings.model_dump()