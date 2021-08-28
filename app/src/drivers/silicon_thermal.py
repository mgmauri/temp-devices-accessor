import random

ramdom_boundary = 1.
initial_temperature = 30.


class SerialPortSiliconThermalDriver:
    def __init__(self, port: str) -> None:
        self._is_open = True
        self._port = port
        self._target_temperature = initial_temperature
        self._reached_temperature = initial_temperature

    @property
    def is_open(self) -> bool:
        return self._is_open

    @property
    def target_temperature(self) -> float:
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value: float) -> None:
        print(f"target_temperature={value}")
        self._target_temperature = value

    @property
    def reached_temperature(self) -> float:
        self._reached_temperature = self._target_temperature + random.uniform(
            -ramdom_boundary,
            ramdom_boundary,
        )
        return self._reached_temperature

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._port})"


if __name__ == "__main__":
    st = SerialPortSiliconThermalDriver(12)
    print(st.reached_temperature)
