import pytest
from src.drivers.gpio import GpioOutputDriver
from src.drivers.silicon_thermal import SerialPortSiliconThermalDriver


@pytest.fixture
def make_gpio_output_driver() -> GpioOutputDriver:
    def _make_gpio_output_driver(pin_number) -> GpioOutputDriver:
        return GpioOutputDriver(pin_number)

    return _make_gpio_output_driver
    # FIXME add del drivers


@pytest.fixture
def make_silicon_thermal_driver():
    def _make_silicon_thermal_driver(port):
        return SerialPortSiliconThermalDriver(port)

    return _make_silicon_thermal_driver
