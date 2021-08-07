import dependency_injector.containers as containers
import dependency_injector.providers as providers
from src.services.gpio_service import GpioOutputDriversService
from src.services.silicon_thermal_service import SiliconThermalDriversService
from src.core.configs import Configs


class SiliconThermalDriversContainer(containers.DeclarativeContainer):
    config = Configs.silicon_thermals_config()
    service = providers.Singleton(
        SiliconThermalDriversService,
        Configs.silicon_thermals_config
    )


class GpioDriversContainer(containers.DeclarativeContainer):
    gpio_config = Configs.gpio_config()
    service = providers.Singleton(
        GpioOutputDriversService,
        Configs.gpio_config
    )
