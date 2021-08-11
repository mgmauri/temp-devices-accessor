import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


class GpioOutputDriver:
	def __init__(self, pin_number: int) -> None:
		self._pin_number = pin_number
		self._value = None
		GPIO.setup(self._pin_number, GPIO.OUT)
		GPIO.output(self._pin_number,True)

	@property
	def value(self) -> bool:
		self._value = GPIO.input(self._pin_number)
		return self._value

	@value.setter
	def value(self, val: bool):
		self._state = val
		GPIO.output(self._pin_number,val)



if __name__ == "__main__":
	pin1 = GpioOutputDriver(pin_number=31)
	pin2 = GpioOutputDriver(pin_number=33)
	pin3 = GpioOutputDriver(pin_number=35)
	pin4 = GpioOutputDriver(pin_number=37)
	pin5 = GpioOutputDriver(pin_number=32)
	pin6 = GpioOutputDriver(pin_number=36)
	pin7 = GpioOutputDriver(pin_number=38)
	pin8 = GpioOutputDriver(pin_number=40)
