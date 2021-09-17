import time
from threading import Timer

from src.core.settings import settings
from src.logger import get_logger
from src.services.gpio_service import GpioOutputDriversService
from src.services.silicon_thermal_service import SiliconThermalDriversService

logger = get_logger(__name__, settings.LOGSPATH)


class WatchdogService:
    def __init__(
        self,
        silicon_thermal_drivers_service: SiliconThermalDriversService,
        gpio_output_drivers_service: GpioOutputDriversService,
        watchdog_interval: float,
        air_blast_duration: float,
        temperature_threshold: float,
        default_temperature: float
    ) -> None:
        self.silicon_thermal_drivers_service = silicon_thermal_drivers_service
        self.gpio_output_drivers_service = gpio_output_drivers_service
        self.watchdog_interval = watchdog_interval
        self.air_blast_duration = air_blast_duration
        self.temperature_threshold = temperature_threshold
        self.default_temperature = default_temperature
        self.timers_by_evk = {}

    def is_valid_evk(self, evk_name: str) -> bool:
        return self.silicon_thermal_drivers_service.is_valid_evk(evk_name)

    def set_target_temperature_by_evk(
        self, evk_name: str, temperature: float
    ) -> None:
        if temperature < self.temperature_threshold:
            self.execute_at_under_threshold_temperature(evk_name, temperature)
        else:
            self.execute_at_above_threshold_temperature(evk_name, temperature)

    def execute_at_under_threshold_temperature(
        self, evk_name: str, temperature: float
    ) -> None:
        timer = self.timers_by_evk.get(evk_name, None)
        if timer is None:
            self.timers_by_evk[evk_name] = Timer(
                interval=self.watchdog_interval,
                function=self.kick,
                args=(evk_name,)
            )
            self.timers_by_evk[evk_name].start()
        self.silicon_thermal_drivers_service.set_target_temperature_by_evk(
                evk_name, temperature
        )

    def execute_at_above_threshold_temperature(
        self, evk_name: str, temperature: float
    ) -> None:
        target_temperature = self.silicon_thermal_drivers_service.\
            get_target_temperature_by_evk(evk_name)
        if target_temperature < 0:
            self._close_timer(evk_name)
            self.air_blast(evk_name)
        self.silicon_thermal_drivers_service.set_target_temperature_by_evk(
                evk_name, temperature
            )

    def air_blast(self, evk_name: str) -> None:
        self.gpio_output_drivers_service.negative_pulse_by_evk(
            evk_name, self.air_blast_duration
        )
        time.sleep(self.air_blast_duration)

    def kick(self, evk_name: str):
        logger.warning(f"{evk_name} was was kicked")
        self._close_timer(evk_name)
        self.air_blast(evk_name)
        self.silicon_thermal_drivers_service.set_target_temperature_by_evk(
                evk_name, self.default_temperature
            )

    def _close_timer(self, evk_name: str) -> None:
        try:
            self.timers_by_evk[evk_name].cancel()
            self.timers_by_evk[evk_name] = None
        except AttributeError:
            logger.critical(
                f"{evk_name} tried to close non existing timer",
                exc_info=True
            )
