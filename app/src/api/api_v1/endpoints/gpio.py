from typing import Any

from fastapi import APIRouter, Depends
from src.api.dependencies import get_gpio_output_drivers_service
from src.api.exceptions import EvkNameNotFound
from src.services.gpio_service import GpioOutputDriversService

router = APIRouter()


@router.get("/gpio_output/{evk_name}")
def get_gpio_output_value(
    evk_name: str,
    gpio_output_drivers_service: GpioOutputDriversService = Depends(
        get_gpio_output_drivers_service
    )
) -> Any:
    if gpio_output_drivers_service.is_valid_evk(evk_name):
        return gpio_output_drivers_service.get_value_by_evk(evk_name)
    else:
        raise EvkNameNotFound


@router.post("/gpio_output/{evk_name}")
def set_gpio_output_value(
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
