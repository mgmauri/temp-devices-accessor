from threading import Timer
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


class GpioOutputDriver:
    def __init__(self, pin_number: int) -> None:
        self._pin_number = pin_number
        self._value = None
        GPIO.setup(self._pin_number, GPIO.OUT)
        GPIO.output(self._pin_number, True)
        self.timer = None

    @property
    def value(self) -> bool:
        self._value = GPIO.input(self._pin_number)
        return self._value

    @value.setter
    def value(self, value: bool):
        self._value = value
        GPIO.output(self._pin_number, value)

    def set_true_value_by_timer(self) -> None:
        self.value = True

    def negative_pulse(self, duration: float = 5) -> None:
        # FIXME add overlaping condition
        self.timer = Timer(duration, self.set_true_value_by_timer).start()
        self.value = False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._pin_number})"


if __name__ == "__main__":
    gpio = GpioOutputDriver(pin_number=31)
