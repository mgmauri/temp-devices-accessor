from typing import Union, MutableMapping

import src.services.base_service as base_service
from src.drivers.gpio import GpioOutputDriver
from src.drivers.temperature import SerialComSiliconThermalDriver


class SiliconThermalDriversService(base_service.BaseService):
    def __init__(self, config_parameters: MutableMapping[int, str]) -> None:
        super().__init__()
        self._silicon_thermal_drivers_by_evk_name = {}
        for com_number, evk_name in config_parameters.items():
            silicon_thermal_driver = SerialComSiliconThermalDriver(com_number)
            try:
                silicon_thermal_driver.connected = True
            except Exception:
                self.logger.error(f"Error on {com_number=}")
                raise(RuntimeError)
            self._silicon_thermal_drivers_by_evk_name[evk_name] = \
                silicon_thermal_driver

    def get_silicon_thermal_driver_by_evk_name(
        self, evk_name: str
    ) -> Union[SerialComSiliconThermalDriver, None]:
        return self._silicon_thermal_drivers_by_evk_name.get(evk_name, None)


class GpioOutputDriversService(base_service.BaseService):
    def __init__(self, config_parameters: MutableMapping[int, str]) -> None:
        super().__init__()
        self._gpio_output_drivers_by_evk_name = {}
        for pin_number, evk_name in config_parameters.items():
            self._gpio_output_drivers_by_evk_name[evk_name] = GpioOutputDriver(
                pin_number
            )
        self.logger.debug("Gpio ouput drivers have been created")

    def get_gpio_output_driver_by_evk_name(
        self, evk_name: str
    ) -> Union[GpioOutputDriver, None]:
        return self._gpio_output_drivers_by_evk_name.get(evk_name, None)
