from typing import Any

from fastapi import APIRouter, Depends
from src.api.dependencies import get_gpio_output_drivers_service
from src.api.exceptions import EvkNameNotFound
from src.services.gpio_service import GpioOutputDriversService

router = APIRouter()


@router.get("/evks/{evk_name}/dryer")
def get_drier_state_by_evk(
    evk_name: str,
    gpio_output_drivers_service: GpioOutputDriversService = Depends(
        get_gpio_output_drivers_service
    )
) -> Any:
    if gpio_output_drivers_service.is_valid_evk(evk_name):
        return gpio_output_drivers_service.get_value_by_evk(evk_name)
    else:
        raise EvkNameNotFound


@router.put("/evks/{evk_name}/dryer")
def set_dryer_state_by_evk(
    evk_name: str,
    value: bool,
    gpio_output_drivers_service: GpioOutputDriversService = Depends(
        get_gpio_output_drivers_service
    )
) -> Any:
    if gpio_output_drivers_service.is_valid_evk(evk_name):
        return gpio_output_drivers_service.set_value_by_evk(
            evk_name, value
        )
    else:
        raise EvkNameNotFound


@router.get("/evks/dryers")
def get_all_evks_dryer_state(
    gpio_output_drivers_service: GpioOutputDriversService = Depends(
        get_gpio_output_drivers_service
    )
) -> Any:
    return gpio_output_drivers_service.get_all_gpio_outputs_value()
