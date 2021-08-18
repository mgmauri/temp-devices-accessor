from typing import Any
from fastapi import APIRouter, Depends
from src.api.dependencies import get_silicon_thermal_drivers_service
from src.services.silicon_thermal_service import SiliconThermalDriversService

router = APIRouter()


@router.get("/evks/{evk_name}/is_valid_evk")
def get_is_valid_evk_name(
    evk_name: str,
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> bool:
    return silicon_thermal_drivers_service.is_valid_evk(
            evk_name
        )


@router.get("/evks")
def get_valid_evk_names(
    silicon_thermal_drivers_service: SiliconThermalDriversService = Depends(
        get_silicon_thermal_drivers_service
    )
) -> Any:
    return set(silicon_thermal_drivers_service.drivers_by_evk_name.keys())
