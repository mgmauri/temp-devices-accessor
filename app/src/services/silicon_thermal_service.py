from typing import Dict, MutableMapping, Optional

import src.services.base_service as base_service
from src.drivers.silicon_thermal import SerialComSiliconThermalDriver


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
        return evk_name in self.drivers_by_evk_name.keys()

    def get_all_silicon_thermals_temperature(self) -> Dict:
        temperatures_by_evk = {}
        for evk_name, driver in self.drivers_by_evk_name.items():
            temperatures_by_evk[evk_name] = driver.temperature
        return temperatures_by_evk
