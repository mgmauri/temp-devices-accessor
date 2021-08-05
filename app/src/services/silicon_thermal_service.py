from typing import MutableMapping, Optional

import src.services.base_service as base_service
from src.drivers.temperature import SerialComSiliconThermalDriver
from src.schemas.temperature import (BaseTemperatureGetter,
                                     BaseTemperatureSetter)


class SiliconThermalDriversService(base_service.BaseService):
    def __init__(
        self, config_parameters: MutableMapping[int, str]
    ) -> None:
        super().__init__()
        self.drivers_by_evk_name = {}
        for com_number, evk_name in config_parameters.items():
            driver = SerialComSiliconThermalDriver(com_number)
            try:
                driver.connected = True
            except Exception:
                self.logger.error(f"Error on {com_number=}")
                raise(RuntimeError)
            self.drivers_by_evk_name[evk_name] = driver
        # FIXME add logs

    def get_driver(
        self, evk_name: str
    ) -> Optional[SerialComSiliconThermalDriver]:
        return self.drivers_by_evk_name.get(evk_name, None)

    def set_temperature_by_evk(
        self, temperature_setter: BaseTemperatureSetter
    ) -> None:
        driver = self.get_driver(temperature_setter.evk_name)
        if driver is not None:
            driver.temperature = temperature_setter.temperature

    def get_temperature_by_evk(
        self, temperature_getter: BaseTemperatureGetter
    ) -> Optional[float]:
        driver = self.get_driver(temperature_getter.evk_name)
        if driver is not None:
            return driver.temperature
        return None
