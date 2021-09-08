import pytest
from src.services.containers import (GpioDriversContainer,
                                     SiliconThermalDriversContainer)
from src.services.gpio_service import GpioOutputDriversService
from src.services.silicon_thermal_service import SiliconThermalDriversService


@pytest.fixture
def gpio_service() -> GpioOutputDriversService:
    return GpioDriversContainer.service()


@pytest.fixture
def silicon_thermal_service() -> SiliconThermalDriversService:
    return SiliconThermalDriversContainer.service()
