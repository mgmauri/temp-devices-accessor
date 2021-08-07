import abc
import logging


class TemperatureDriver(abc.ABC):
    def __init__(self) -> None:
        self.logger = logging.getLogger(
            f'{__name__}.{self.__class__.__name__}',
        )
        self._connected = None

    @property
    def connected(self):
        return self._connected

    @connected.setter
    def connected(self, val: bool):
        self._connected = val

    @property
    def temperature(self) -> None:
        return None

    @temperature.setter
    def temperature(self, val: float) -> None:
        pass


class SerialComSiliconThermalDriver(TemperatureDriver):
    def __init__(self, com_number: int) -> None:
        super().__init__()
        self._com_number = com_number
        self._temperature = None
        self.logger.debug(f"SerialComSiliconThermalDriver({com_number=})")

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, val: float) -> None:
        self._temperature = val

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._com_number})"


if __name__ == "__main__":
    print("Hi VSCODE")
    st = SerialComSiliconThermalDriver(12)
