from typing import Any

from src.api.dependencies import get_silicon_thermal_drivers_service
from fastapi import APIRouter, Depends
from src.services.silicon_thermal_service import SiliconThermalDriversService
from src.api.exceptions import EvkNameNotFound

router = APIRouter()


@router.get("/evks/{evk_name}/silicon_thermal/reached_temperature")
def get_reached_temperature_by_evk(
    evk_name: str,
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    if silicon_thermal_drivers_service.is_valid_evk(evk_name):
        return silicon_thermal_drivers_service.get_reached_temperature_by_evk(
            evk_name
        )
    else:
        raise EvkNameNotFound


@router.put("/evks/{evk_name}/silicon_thermal/target_temperature")
def set_target_temperature_by_evk(
    evk_name: str,
    temperature: float,
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    if silicon_thermal_drivers_service.is_valid_evk(evk_name):
        return silicon_thermal_drivers_service.set_target_temperature_by_evk(
            evk_name, temperature
        )
    else:
        raise EvkNameNotFound


@router.get("/evks/{evk_name}/silicon_thermal/target_temperature")
def get_target_temperature_by_evk(
    evk_name: str,
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    if silicon_thermal_drivers_service.is_valid_evk(evk_name):
        return silicon_thermal_drivers_service.get_target_temperature_by_evk(
            evk_name
        )
    else:
        raise EvkNameNotFound


@router.get("/evks/silicon_thermal/reached_temperatures")
def get_reached_temperatures(
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    print(hex(id(silicon_thermal_drivers_service)))
    return silicon_thermal_drivers_service.get_reached_temperatures()


@router.get("/evks/silicon_thermal/target_temperatures")
def get_target_temperatures(
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    print(hex(id(silicon_thermal_drivers_service)))
    return silicon_thermal_drivers_service.get_target_temperatures()
