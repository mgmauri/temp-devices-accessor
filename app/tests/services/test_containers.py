from src.services.containers import (GpioDriversContainer,
                                     SiliconThermalDriversContainer,
                                     WatchdogContainer)


def test_silicon_thermals_drivers_container():
    service_1 = SiliconThermalDriversContainer.service()
    service_2 = SiliconThermalDriversContainer.service()
    assert service_1 is service_2


def test_gpio_drivers_container():
    service_1 = GpioDriversContainer.service()
    service_2 = GpioDriversContainer.service()
    assert service_1 is service_2


def test_watchdog_container():
    service_1 = WatchdogContainer.service()
    service_2 = WatchdogContainer.service()
    assert service_1 is service_2
