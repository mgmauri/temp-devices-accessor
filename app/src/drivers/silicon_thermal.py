class SerialPortSiliconThermalDriver:
    def __init__(self, port: str) -> None:
        self._connected = None
        self._port = port
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
        return f"{self.__class__.__name__}({self._port})"


if __name__ == "__main__":
    st = SerialPortSiliconThermalDriver(12)
