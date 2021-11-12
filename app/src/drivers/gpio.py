from threading import Timer


class GpioOutputDriver:
    def __init__(self, pin_number: int) -> None:
        self._pin_number = pin_number
        self._value = None
        self.timer = None

    @property
    def value(self) -> bool:
        # code to read pin state or just return internal variable self._state
        return self._value

    @value.setter
    def value(self, value: bool):
        # code to set pin state
        print(f"PIN{self._pin_number}={value}")
        self._value = value

    def set_true_value(self) -> None:
        self.value = True

    def negative_pulse(self, duration: float = 5) -> None:
        # FIXME add overlaping condition
        self.value = False
        self.timer = Timer(duration, self.set_true_value).start()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._pin_number})"


if __name__ == "__main__":
    gpio = GpioOutputDriver(pin_number=2)
