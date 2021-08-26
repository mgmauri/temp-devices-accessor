from typing import Iterable
from src.core.configs import DriversConfig


def get_gpio_output_pin_numbers() -> Iterable:
    return DriversConfig.gpio_config().values()


def get_silicon_thermal_ports() -> Iterable:
    return DriversConfig.silicon_thermals_config.values()
