from src.services.containers import (GpioDriversContainer,
                                     GpioOutputDriversService,
                                     SiliconThermalDriversContainer,
                                     SiliconThermalDriversService)


def get_silicon_thermal_drivers_service() -> SiliconThermalDriversService:
    silicon_thermal_drivers_service = SiliconThermalDriversContainer.service()
    return silicon_thermal_drivers_service


def get_gpio_output_drivers_service() -> GpioOutputDriversService:
    gpio_output_drivers_service = GpioDriversContainer.service()
    return gpio_output_drivers_service


if __name__ == "__main__":
    st_s = get_silicon_thermal_drivers_service()
