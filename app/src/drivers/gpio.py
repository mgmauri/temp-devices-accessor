class GpioOutputDriver:
    def __init__(self, pin_number: int) -> None:
        self._pin_number = pin_number
        self._state = None

    @property
    def value(self) -> bool:
        # code to read pin state or just return internal variable self._state
        return self._state

    @value.setter
    def value(self, value: bool):
        # code to set pin state
        self._state = value


if __name__ == "__main__":
    relays_controller = GpioOutputDriver(pin_number=2)
    relays_controller.relay_0_status
