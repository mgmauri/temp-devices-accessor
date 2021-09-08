import pytest
from tests.utils import (silicon_thermals_evk_names,
                         silicon_thermal_temperature_range)


silicon_thermal_timeout = 100


@pytest.mark.parametrize("evk_name", silicon_thermals_evk_names())
def test_set_valid_target_temperature_by_evk(
    silicon_thermal_service, evk_name: str
):
    import random
    target_temperature = random.uniform(-5, 100)   # FIXME add config
    silicon_thermal_service.set_target_temperature_by_evk(
        evk_name, target_temperature
    )
    assert silicon_thermal_service.get_target_temperature_by_evk(
        evk_name
        ) == target_temperature


@pytest.mark.parametrize("evk_name", silicon_thermals_evk_names())
def test_reached_temperature_by_evk(
    silicon_thermal_service, evk_name: str
):
    import random
    import math
    import time
    target_temperature = random.uniform(
        *silicon_thermal_temperature_range()
    )
    silicon_thermal_service.set_target_temperature_by_evk(
        evk_name, target_temperature
    )
    for _ in range(silicon_thermal_timeout):
        time.sleep(1)
        is_close = math.isclose(
            silicon_thermal_service.get_reached_temperature_by_evk(evk_name),
            target_temperature,
            rel_tol=0.05
        )
        if is_close:
            assert True
            break
    else:
        assert False
