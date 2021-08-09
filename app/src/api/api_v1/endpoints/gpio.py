from typing import Any

from fastapi import APIRouter, Depends
from src.api.dependencies import get_gpio_drivers_service
from src.api.exceptions import EvkNameNotFound
from src.services.gpio_service import GpioOutputDriversService

router = APIRouter()


@router.get("/gpio/{evk_name}")
def get_gpio_value(
    evk_name: str,
    gpio_service: GpioOutputDriversService = Depends(
        get_gpio_drivers_service
    )
) -> Any:
    print(f"{gpio_service.is_valid_evk(evk_name)=}")
    if gpio_service.is_valid_evk(evk_name):
        return gpio_service.get_value_by_evk(evk_name)
    else:
        raise EvkNameNotFound


@router.post("/gpio/{evk_name}")
def set_gpio_gpio(
    evk_name: str,
    value: bool,
    gpio_service: GpioOutputDriversService = Depends(
        get_gpio_drivers_service
    )
) -> Any:
    if gpio_service.is_valid_evk(evk_name):
        return gpio_service.set_value_by_evk(
            evk_name, value
        )
    else:
        raise EvkNameNotFound
