import pytest
from src.services.containers import (GpioDriversContainer,
                                     SiliconThermalDriversContainer,
                                     WatchdogContainer)
from src.services.gpio_service import GpioOutputDriversService
from src.services.silicon_thermal_service import SiliconThermalDriversService
from src.services.watchdog_service import WatchdogService


@pytest.fixture
def gpio_service() -> GpioOutputDriversService:
    return GpioDriversContainer.service()


@pytest.fixture
def silicon_thermal_service() -> SiliconThermalDriversService:
    return SiliconThermalDriversContainer.service()


@pytest.fixture
def watchdog_service() -> WatchdogService:
    return WatchdogContainer.service()
