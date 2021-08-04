import dependency_injector.containers as containers
import dependency_injector.providers as providers
from src.services.drivers_access_services import (
    GpioOutputDriversService, SiliconThermalDriversService)


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


if __name__ == "__main__":
    st_file_path = "../config/silicon_thermals_config.yaml"
    Configs.silicon_thermals_config.from_yaml(st_file_path)
    st_service = SiliconThermalDriversContainer.service()
    st_driver = st_service.get_silicon_thermal_driver_by_evk_name("tiger_99")

    gpio_file_path = "../config/gpio_config.yaml"
    Configs.gpio_config.from_yaml(gpio_file_path)
    gpio_service = GpioDriversContainer.service()
