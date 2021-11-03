import dependency_injector.containers as containers
import dependency_injector.providers as providers
from src.core.configs import DriversConfig, OperationConfig
from src.services.gpio_service import GpioOutputDriversService
from src.services.silicon_thermal_service import SiliconThermalDriversService
from src.services.watchdog_service import WatchdogService


class SiliconThermalDriversContainer(containers.DeclarativeContainer):
    config = DriversConfig.silicon_thermals_config()
    service = providers.Singleton(
        SiliconThermalDriversService, DriversConfig.silicon_thermals_config
    )


class GpioDriversContainer(containers.DeclarativeContainer):
    gpio_config = DriversConfig.gpio_config()
    service = providers.Singleton(GpioOutputDriversService, DriversConfig.gpio_config)


class WatchdogContainer(containers.DeclarativeContainer):
    silicon_thermal_drivers_service = SiliconThermalDriversContainer.service()
    gpio_output_drivers_service = GpioDriversContainer.service()
    service = providers.Singleton(
        WatchdogService,
        silicon_thermal_drivers_service=silicon_thermal_drivers_service,
        gpio_output_drivers_service=gpio_output_drivers_service,
        air_blast_duration=OperationConfig.config.air_blast_default_duration,
        watchdog_interval=OperationConfig.config.watchdog_interval,
        temperature_threshold=OperationConfig.config.temperature_threshold,
        default_temperature=OperationConfig.config.default_temperature,
    )
