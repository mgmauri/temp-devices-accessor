from typing import Iterable
from src.core.configs import DriversConfig
from src.core.configs import OperationConfig


def gpio_output_pin_numbers() -> Iterable:
    return DriversConfig.gpio_config().values()


def silicon_thermal_ports() -> Iterable:
    return DriversConfig.silicon_thermals_config().values()


def silicon_thermal_temperature_range():
    minimum_temperature = OperationConfig.config().get(
        "minimum_temperature", 0
    )
    maximum_temperature = OperationConfig.config().get(
        "maximum_temperature", 100
    )
    return minimum_temperature, maximum_temperature


def gpio_evk_names() -> Iterable:
    return DriversConfig.gpio_config().keys()


def silicon_thermals_evk_names() -> Iterable:
    return DriversConfig.silicon_thermals_config().keys()
