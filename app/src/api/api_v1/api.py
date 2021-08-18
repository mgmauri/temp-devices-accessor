from fastapi import APIRouter
from src.api.api_v1.endpoints import dryer, silicon_thermal, config_info

api_router = APIRouter()
api_router.include_router(silicon_thermal.router, tags=["Silicon Thermals"])
api_router.include_router(dryer.router, tags=["Dryers"])
api_router.include_router(config_info.router, tags=["Config Information"])
