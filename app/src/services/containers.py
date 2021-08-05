import dependency_injector.containers as containers
import dependency_injector.providers as providers

from src.core.settings import settings
from src.services.silicon_thermal_service import SiliconThermalDriversService
from src.services.gpio_service import GpioOutputDriversService


class Configs(containers.DeclarativeContainer):
    silicon_thermals_config = providers.Configuration()
    gpio_config = providers.Configuration()


class SiliconThermalDriversContainer(containers.DeclarativeContainer):
    config = Configs.silicon_thermals_config()
    service = providers.Singleton(
        SiliconThermalDriversService,
        Configs.silicon_thermals_config
    )


class GpioDriversContainer(containers.DeclarativeContainer):
    config = Configs.gpio_config()
    service = providers.Singleton(
        GpioOutputDriversService,
        Configs.gpio_config
    )


Configs.silicon_thermals_config.from_yaml(settings.SILICONTHERMALSCONFIG)
Configs.gpio_config.from_yaml(settings.GPIOCONFIG)
