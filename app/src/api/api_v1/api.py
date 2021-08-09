from fastapi import APIRouter
from src.api.api_v1.endpoints import gpio, temperature

api_router = APIRouter()
api_router.include_router(temperature.router, tags=["temperature"])
api_router.include_router(gpio.router, tags=["gpio"])
