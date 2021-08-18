import time

import serial


class SiliconThermalSerialPortDriver:
    def __init__(self, port: str) -> None:
        self.dev = serial.Serial(port, write_timeout=5.0)
        self._target_temperature = None

    @property
    def is_open(self) -> bool:
        return self.dev.is_open

    @property
    def target_temperature(self) -> float:
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value: float) -> None:
        print('1st - value:', value, 'Type:', type(value))
        sign = "00" if value >= 0 else "FF"
        value = "%0.1f" % abs(value)
        self._target_temperature = value
        # code to set silicon thermal temperature
        print('2nd - value:', value, 'Type:', type(value))
        code_temp = value
        code_int = '%03d' % int(code_temp.split('.')[0])
        code_dec = '%01d' % int(code_temp.split('.')[1])
        print('code_int + code_dec:', code_int + code_dec)

        temp_code = code_int+code_dec
        protocol = 'L'
        ctrl_addr = '01'
        change_setp = '0200'
        cs_code = ''.join([ctrl_addr, change_setp, temp_code, sign])
        print('cs_code:', cs_code)
        check_sum = self._calculate_checksum(cs_code)
        cmd = chr(2) + protocol + cs_code + check_sum + chr(3)
        print('CMD:', cmd)
        self.dev.flushInput()
        self.dev.flushOutput()
        print('Return:', self.dev.write(cmd.encode()))

    def _calculate_checksum(self, cs_code):
        # This function calculates the checksum required by ICS unit
        val = 0
        for c in range(len(cs_code)):
            val = val + ord(cs_code[c])
        str = hex(val)[2:]
        checksum = str[len(str)-2] + str[len(str)-1]
        print('Checksum', checksum)
        return checksum

    @property
    def reached_temperature(self) -> float:
        self.dev.flushInput()
        self.dev.flushOutput()
        cmd = f"{chr(2)}L0100C1{chr(3)}".encode()
        self.dev.write(cmd)
        time.sleep(.1)
        rsp = self.dev.read_all()
        sign = -1 if rsp[7] == "5" else 1
        reached_temperature = (float(rsp[8:11]) + float(rsp[11]/100)) * sign
        return reached_temperature
