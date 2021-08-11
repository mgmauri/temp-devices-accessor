class SerialComSiliconThermalDriver:
    def __init__(self, com_number: int) -> None:
        self._connected = None
        self._com_number = com_number
        self._temperature = None

    @property
    def connected(self):
        return self._connected

    @connected.setter
    def connected(self, value: bool) -> None:
        self._connected = value

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, val: float) -> None:
        self._temperature = val

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._com_number})"


if __name__ == "__main__":
    st = SerialComSiliconThermalDriver(12)
