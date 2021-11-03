from typing import Iterable
from src.core.configs import DriversConfig
from src.core.configs import OperationConfig
import random

silicon_thermal_timeout = 100  # FIXME add config
maximum_temperature = OperationConfig.config().get("maximum_temperature", 100)
minimum_temperature = OperationConfig.config().get("minimum_temperature", 0)
temperature_threshold = OperationConfig.config.get("temperature_threshold", 0)


def gpio_output_pin_numbers() -> Iterable:
    return DriversConfig.gpio_config().values()


def silicon_thermal_ports() -> Iterable:
    return DriversConfig.silicon_thermals_config().values()


def gpio_evk_names() -> Iterable:
    return DriversConfig.gpio_config().keys()


def silicon_thermals_evk_names() -> Iterable:
    return DriversConfig.silicon_thermals_config().keys()


def valid_random_temperature() -> float:
    return random.uniform(minimum_temperature, maximum_temperature)


def above_threshold_random_temperature() -> float:
    return random.uniform(temperature_threshold, maximum_temperature)


def below_threshold_random_temperature() -> float:
    return random.uniform(minimum_temperature, temperature_threshold)
