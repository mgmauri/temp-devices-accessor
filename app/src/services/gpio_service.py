from typing import Dict, MutableMapping, Optional

import src.services.base_service as base_service
from src.drivers.gpio import GpioOutputDriver


class GpioOutputDriversService(base_service.BaseService):
    def __init__(
        self, config_parameters: MutableMapping[int, str]
    ) -> None:
        super().__init__()
        self.drivers_by_evk_name = {}
        for evk_name, pin_number in config_parameters.items():
            self.drivers_by_evk_name[evk_name] = GpioOutputDriver(
                pin_number
            )
        # FIXME add logs

    def _get_driver(
        self, evk_name: str
    ) -> Optional[GpioOutputDriver]:
        return self.drivers_by_evk_name.get(evk_name, None)

    def negative_pulse_by_evk(self, evk_name, width: float) -> None:
        driver = self._get_driver(evk_name)
        if driver is not None:
            driver.negative_pulse(width)

    def set_value_by_evk(
        self, evk_name: str, value: bool
    ) -> None:
        driver = self._get_driver(evk_name)
        if driver is not None:
            driver.value = value

    def get_value_by_evk(
        self, evk_name: str
    ) -> Optional[bool]:
        driver = self._get_driver(evk_name)
        if driver is not None:
            return driver.value
        return None

    def is_valid_evk(self, evk_name: str) -> bool:
        return evk_name in self.drivers_by_evk_name.keys()

    def get_all_gpio_outputs_value(self) -> Dict:
        values_by_evk = {}
        for evk_name, driver in self.drivers_by_evk_name.items():
            values_by_evk[evk_name] = driver.value
        return values_by_evk
