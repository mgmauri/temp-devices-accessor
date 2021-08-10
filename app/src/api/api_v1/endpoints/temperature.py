from typing import Any

from src.api.dependencies import get_silicon_thermal_drivers_service
from fastapi import APIRouter, Depends
from src.services.silicon_thermal_service import SiliconThermalDriversService
from src.api.exceptions import EvkNameNotFound

router = APIRouter()


@router.get("/temperature/{evk_name}")
def get_temperature(
    evk_name: str,
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    if silicon_thermal_drivers_service.is_valid_evk(evk_name):
        return silicon_thermal_drivers_service.get_temperature_by_evk(evk_name)
    else:
        raise EvkNameNotFound


@router.post("/temperature/{evk_name}")
def set_temperature(
    evk_name: str,
    temperature: float,
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    if silicon_thermal_drivers_service.is_valid_evk(evk_name):
        return silicon_thermal_drivers_service.set_temperature_by_evk(
            evk_name, temperature
        )
    else:
        raise EvkNameNotFound
