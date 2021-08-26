import pytest
from src.drivers.gpio import GpioOutputDriver


@pytest.fixture
def make_gpio_output_driver() -> GpioOutputDriver:
    def _make_gpio_output_driver(pin_number):
        return GpioOutputDriver(pin_number)

    return _make_gpio_output_driver
    # FIXME add del drivers
