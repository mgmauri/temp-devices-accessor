from threading import Timer


class GpioOutputDriver:
    def __init__(self, pin_number: int) -> None:
        self._pin_number = pin_number
        self._value = None

    @property
    def value(self) -> bool:
        # code to read pin state or just return internal variable self._state
        return self._value

    @value.setter
    def value(self, value: bool):
        # code to set pin state
        print(f"PIN{self._pin_number}={value}")
        self._value = value

    def set_value(self, value: bool) -> None:
        self.value = value

    def negative_pulse(self, width: float = 5) -> None:
        Timer(width, self.set_value, args=(True,)).start()
        self.value = False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._pin_number})"


if __name__ == "__main__":
    gpio = GpioOutputDriver(pin_number=2)
