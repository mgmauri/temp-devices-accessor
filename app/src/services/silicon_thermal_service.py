from typing import Dict, MutableMapping, Optional
from src.drivers.silicon_thermal import SerialPortSiliconThermalDriver


class SiliconThermalDriversService:
    def __init__(
        self, config_parameters: MutableMapping[int, str]
    ) -> None:
        self.drivers_by_evk_name = {}
        for evk_name, port in config_parameters.items():
            driver = SerialPortSiliconThermalDriver(port)
            try:
                driver.connected = True
            except Exception:
                raise(RuntimeError)
            self.drivers_by_evk_name[evk_name] = driver

    def _get_driver(
        self, evk_name: str
    ) -> Optional[SerialPortSiliconThermalDriver]:
        return self.drivers_by_evk_name.get(evk_name, None)

    def set_target_temperature_by_evk(
        self, evk_name: str, temperature: float
    ) -> None:
        driver = self._get_driver(evk_name)
        if driver is not None:
            driver.target_temperature = temperature

    def get_target_temperature_by_evk(self, evk_name: str) -> Optional[float]:
        driver = self._get_driver(evk_name)
        if driver is not None:
            return driver.target_temperature
        return None

    def get_target_temperatures(self) -> Dict:
        return {
            evk_name: driver.target_temperature
            for evk_name, driver in self.drivers_by_evk_name.items()
        }

    def get_reached_temperature_by_evk(self, evk_name: str) -> Optional[float]:
        driver = self._get_driver(evk_name)
        if driver is not None:
            return driver.reached_temperature
        return None

    def get_reached_temperatures(self) -> Dict:
        return {
            evk_name: driver.reached_temperature
            for evk_name, driver in self.drivers_by_evk_name.items()
        }

    def is_valid_evk(self, evk_name: str) -> bool:
        return evk_name in self.drivers_by_evk_name.keys()
