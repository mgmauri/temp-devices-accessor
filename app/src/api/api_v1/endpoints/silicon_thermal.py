from typing import Any

from fastapi import APIRouter, Depends
from fastapi.param_functions import Query
from src.api.dependencies import get_silicon_thermal_drivers_service
from src.api.exceptions import EvkNameNotFound
from src.core.configs import OperationConfig
from src.services.silicon_thermal_service import SiliconThermalDriversService

router = APIRouter()


@router.put("/drivers/silicon_thermals/{evk_name}/target_temperature")
def set_target_temperature_by_evk(
    evk_name: str,
    temperature: float = Query(...,
                               gt=OperationConfig.config.minimum_temperature(),
                               lt=OperationConfig.config.maximum_temperature()
                               ),
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


@router.get("/drivers/silicon_thermals/{evk_name}/target_temperature")
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


@router.get("/drivers/silicon_thermals/{evk_name}/reached_temperature")
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


@router.get("/drivers/silicon_thermals/reached_temperatures")
def get_reached_temperatures(
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    print(hex(id(silicon_thermal_drivers_service)))
    return silicon_thermal_drivers_service.get_reached_temperatures()


@router.get("/drivers/silicon_thermals/target_temperatures")
def get_target_temperatures(
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    print(hex(id(silicon_thermal_drivers_service)))
    return silicon_thermal_drivers_service.get_target_temperatures()
