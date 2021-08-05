from typing import MutableMapping, Optional

import src.services.base_service as base_service
from src.drivers.gpio import GpioOutputDriver
from src.schemas.gpio import BaseGpioGetter, BaseGpioSetter


class GpioOutputDriversService(base_service.BaseService):
    def __init__(
        self, config_parameters: MutableMapping[int, str]
    ) -> None:
        super().__init__()
        self.drivers_by_evk_name = {}
        for pin_number, evk_name in config_parameters.items():
            self.drivers_by_evk_name[evk_name] = GpioOutputDriver(
                pin_number
            )
        # FIXME add logs

    def get_driver_by_evk_name(
        self, evk_name: str
    ) -> Optional[GpioOutputDriver]:
        return self.drivers_by_evk_name.get(evk_name, None)

    def get_value_by_evk(
        self, gpio_getter: BaseGpioGetter
    ) -> Optional[bool]:
        driver = self.get_drivers_by_evk_name(gpio_getter.evk_name)
        if driver is not None:
            return driver.value
        return None
    
    def set_value_by_evk(
        self, gpio_setter: BaseGpioSetter
    ) -> None:
        driver = self.get_drivers_by_evk_name(gpio_setter.evk_name)
        if driver is not None:
            driver.value = gpio_setter.value
