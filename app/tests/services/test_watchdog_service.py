import pytest
from tests.utils import (
    silicon_thermal_timeout,
    silicon_thermals_evk_names,
    valid_random_temperature,
)


@pytest.mark.parametrize("evk_name", silicon_thermals_evk_names())
def test_set_below_threshold_target_temperature_by_evk(
    watchdog_service, silicon_thermal_service, evk_name
):
    import time
    import math

    target_temperature = valid_random_temperature()
    watchdog_service.set_target_temperature_by_evk(evk_name, target_temperature)
    for _ in range(silicon_thermal_timeout):
        time.sleep(1)
        is_close = math.isclose(
            silicon_thermal_service.get_reached_temperature_by_evk(evk_name),
            target_temperature,
            rel_tol=0.05,
        )
        if is_close:
            assert True
            break
    else:
        assert False
