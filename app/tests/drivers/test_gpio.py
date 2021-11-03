import pytest
from tests.utils import gpio_output_pin_numbers
import threading
import time


@pytest.mark.parametrize("pin_number", gpio_output_pin_numbers())
def test_gpio_output_true_value(make_gpio_output_driver, pin_number: int):
    gpio_output_driver = make_gpio_output_driver(pin_number)
    gpio_output_driver.value = True
    assert gpio_output_driver.value


@pytest.mark.parametrize("pin_number", gpio_output_pin_numbers())
def test_gpio_output_false_value(make_gpio_output_driver, pin_number: int):
    gpio_output_driver = make_gpio_output_driver(pin_number)
    gpio_output_driver.value = False
    assert not gpio_output_driver.value


@pytest.mark.parametrize("pin_number", gpio_output_pin_numbers())
def test_gpio_set_true_value(make_gpio_output_driver, pin_number):
    gpio_output_driver = make_gpio_output_driver(pin_number)
    gpio_output_driver.set_true_value()
    assert gpio_output_driver.value


@pytest.mark.parametrize("pin_number", gpio_output_pin_numbers())
def test_negative_pulse(make_gpio_output_driver, pin_number):
    gpio_output_driver = make_gpio_output_driver(pin_number)
    thread = threading.Thread(target=gpio_output_driver.negative_pulse)
    thread.start()
    time.sleep(1)
    assert not gpio_output_driver.value
    time.sleep(10)  # FIXME add config
    assert gpio_output_driver.value
