from typing import MutableMapping, Optional

import src.services.base_service as base_service
from src.drivers.temperature import SerialComSiliconThermalDriver


class SiliconThermalDriversService(base_service.BaseService):
    def __init__(
        self, config_parameters: MutableMapping[int, str]
    ) -> None:
        super().__init__()
        self.drivers_by_evk_name = {}
        for evk_name, com_number in config_parameters.items():
            driver = SerialComSiliconThermalDriver(com_number)
            try:
                driver.connected = True
            except Exception:
                self.logger.error(f"Error on {com_number=}")
                raise(RuntimeError)
            self.drivers_by_evk_name[evk_name] = driver
        # FIXME add logs

    def _get_driver(
        self, evk_name: str
    ) -> Optional[SerialComSiliconThermalDriver]:
        return self.drivers_by_evk_name.get(evk_name, None)

    def set_temperature_by_evk(
        self, evk_name: str, temperature: float
    ) -> None:
        driver = self._get_driver(evk_name)
        if driver is not None:
            driver.temperature = temperature

    def get_temperature_by_evk(
        self, evk_name: str
    ) -> Optional[float]:
        driver = self._get_driver(evk_name)
        if driver is not None:
            return driver.temperature
        return None

    def is_valid_evk(self, evk_name: str) -> bool:
        print(f"evks={self.drivers_by_evk_name.keys()}")
        return evk_name in self.drivers_by_evk_name.keys()
