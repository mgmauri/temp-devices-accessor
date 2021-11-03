import pytest
import threading
from tests.utils import gpio_evk_names
import time


@pytest.mark.parametrize("evk_name", gpio_evk_names())
def test_negative_pulse_by_evk(gpio_service, evk_name: str):
    thread = threading.Thread(
        target=gpio_service.negative_pulse_by_evk,
        args=(evk_name, 2),  # FIXME add config
    )
    thread.start()
    time.sleep(1)
    assert not gpio_service.get_value_by_evk(evk_name)
    time.sleep(10)  # FIXME add config
    assert gpio_service.get_value_by_evk(evk_name)


@pytest.mark.parametrize("evk_name", gpio_evk_names())
def test_set_true_value_by_evk(gpio_service, evk_name: str):
    gpio_service.set_value_by_evk(evk_name, True)
    assert gpio_service.get_value_by_evk(evk_name)


@pytest.mark.parametrize("evk_name", gpio_evk_names())
def test_set_false_value_by_evk(gpio_service, evk_name: str):
    gpio_service.set_value_by_evk(evk_name, False)
    assert not gpio_service.get_value_by_evk(evk_name)
