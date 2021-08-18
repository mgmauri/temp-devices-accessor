import dependency_injector.containers as containers
import dependency_injector.providers as providers
from src.services.gpio_service import GpioOutputDriversService
from src.services.silicon_thermal_service import SiliconThermalDriversService
from src.core.configs import DriversConfig


class SiliconThermalDriversContainer(containers.DeclarativeContainer):
    config = DriversConfig.silicon_thermals_config()
    service = providers.Singleton(
        SiliconThermalDriversService,
        DriversConfig.silicon_thermals_config
    )


class GpioDriversContainer(containers.DeclarativeContainer):
    gpio_config = DriversConfig.gpio_config()
    service = providers.Singleton(
        GpioOutputDriversService,
        DriversConfig.gpio_config
    )
