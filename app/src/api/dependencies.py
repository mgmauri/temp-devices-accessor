from src.services.containers import (GpioDriversContainer,
                                     GpioOutputDriversService,
                                     SiliconThermalDriversContainer,
                                     SiliconThermalDriversService)


def get_silicon_thermal_drivers_service() -> SiliconThermalDriversService:
    silicon_thermal_drivers_service = SiliconThermalDriversContainer.service()
    return silicon_thermal_drivers_service


def get_gpio_drivers_service() -> GpioOutputDriversService:
    gpio_drivers_service = GpioDriversContainer.service()
    return gpio_drivers_service
