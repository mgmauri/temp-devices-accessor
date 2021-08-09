from typing import MutableMapping, Optional

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
        print(f"evks={self.drivers_by_evk_name.keys()}")
        return evk_name in self.drivers_by_evk_name.keys()
