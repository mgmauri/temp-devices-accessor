from fastapi import APIRouter
from src.api.api_v1.endpoints import gpio, silicon_thermal

api_router = APIRouter()
api_router.include_router(silicon_thermal.router, tags=["silicon_thermal"])
api_router.include_router(gpio.router, tags=["gpio"])
