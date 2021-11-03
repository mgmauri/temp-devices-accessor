import pytest
from tests.utils import silicon_thermal_ports, valid_random_temperature

silicon_thermal_timeout = 60


@pytest.mark.parametrize("port", silicon_thermal_ports())
def test_is_open(make_silicon_thermal_driver, port: str):
    silicon_thermal_driver = make_silicon_thermal_driver(port)
    assert silicon_thermal_driver.is_open


@pytest.mark.parametrize("port", silicon_thermal_ports())
def test_target_temperature(make_silicon_thermal_driver, port: str):
    silicon_thermal_driver = make_silicon_thermal_driver(port)
    temperature = valid_random_temperature()
    silicon_thermal_driver.target_temperature = temperature
    assert silicon_thermal_driver.target_temperature == temperature


@pytest.mark.parametrize("port", silicon_thermal_ports())
def test_reached_temperature(make_silicon_thermal_driver, port: str):
    import math
    import time

    silicon_thermal_driver = make_silicon_thermal_driver(port)
    target_temperature = valid_random_temperature()
    silicon_thermal_driver.target_temperature = target_temperature
    for _ in range(silicon_thermal_timeout):
        time.sleep(1)
        is_close = math.isclose(
            silicon_thermal_driver.reached_temperature, target_temperature, rel_tol=0.05
        )
        if is_close:
            assert True
            break
    else:
        assert False
