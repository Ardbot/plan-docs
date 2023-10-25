# LLS протокол для ДУТ и т.п. устройств на базе RS-485

# Переходник RS-485 подключается паралленьно мастеру и рабу и захватывает данные (только для отладки)

import serial   # Serial port (COM port)
import time

ser = serial.Serial()

ser.baudrate = 19200  # Будь внимательнее!

ser.timeout = 0


def connectToPort(port='COM1'):
    """ Подключение к порту """
    try:
        ser.port = port
        ser.open()
        time.sleep(1)   # Ожидание первого сообщения
        print(f'Connect to {port}')
        while True:

            while ser.in_waiting > 0:

                data = ser.readline()
                print(data.hex())  # Выводим данные в консоль
                time.sleep(0.2)
                # write_port(b'310006A8')
            # print("Ожидаю данные")
            time.sleep(0.2)

        return (True, f"Подключено к {ser.name}")

    except serial.SerialException as e:
        return print(False, f"Ошибка подключения к {ser.name}.\n. Err: {e}")


def write_port(code):
    """ Отправляем данные в порт и получаем ответ"""
    try:

        ser.write(code.encode())
        time.sleep(0.1)
        data = ser.readline()   # Читаем ответ
        line = data.decode("utf-8")
        # log(f"{code}: {line}")
        print(line)

        return (True, line)

    except Exception as e:
        return (False, str(e))


connectToPort("COM5")


# Функция подсчета контрольной суммы
# pass


# Перехваченные данные между Мастером и Рабом (Для примера)

#  С Rfid картой

"""
31 01 06 6C
3E 01 06 00 00 00 00 00 CA

31 00 06 A8 
3E 00 06 E4 5C 3E 00 00 D2 

31 01 06 6C 
3E 01 06 00 00 00 00 00 CA 

...

"""

# Без карты
"""
31 00 06 A8 
3E 00 06 00 00 00 00 00 F7 

31 01 06 6C 
3E 01 06 00 00 00 00 00 CA 

31 FF 31 01 06 6C 

31 00 06 A8 
3E 00 06 00 00 00 00 00 F7 

...

"""

# Строки с python
"""
310006a83e0006e45c3e0000d2
3101066c3e01060000000000ca

# Мастер        Раб
31 00 06 a8     3e 00 06 e4 5c 3e 00 00 d2
31 01 06 6c     3e 01 06 00 00 00 00 00 ca

....

"""
