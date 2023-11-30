# LLS протокол для ДУТ и т.п. устройств на базе RS-485

# Переходник RS-485 подключается паралленьно мастеру и рабу и захватывает данные (только для отладки)

import serial   # Serial port (COM port)
import time
import re

ser = serial.Serial()

ser.baudrate = 19200  # Будь внимательнее!

ser.timeout = 0


def getLLS(data='31 00 06 A8'):  # Запрос
    "Запрос в COM port"
    print("GET:", data)  # '31 00 06 A8'
    result = bytes.fromhex(data)  # Преобразуем в байты
    # print(result)
    ser.write(result)  # Отравляем данные в порт


def parsLLS(data):  # Ответ
    # print(data)
    "Разбор ответа"
    data = data.hex()
    # print('hex:', data)
    n = 2

    # Развибка по байтам ['3e', '00', '06', 'e4', '5c', '3e', '00', '00', 'd2']
    data = re.findall('.{%s}' % n, data)
    print("RESPONSE:", data)


def crc8(data, crc):
    "Просчет контрольной суммы табличным методом"
    for byte in data:
        i = byte ^ crc
        crc = 0
        if i & 0x01:
            crc ^= 0x5e
        if i & 0x02:
            crc ^= 0xbc
        if i & 0x04:
            crc ^= 0x61
        if i & 0x08:
            crc ^= 0xc2
        if i & 0x10:
            crc ^= 0x9d
        if i & 0x20:
            crc ^= 0x23
        if i & 0x40:
            crc ^= 0x46
        if i & 0x80:
            crc ^= 0x8c

    return crc


# Примеры использования. Проверить онлайн `https://crccalc.com/?crc=0x31%200x01%200x06&method=crc8&datatype=hex&outtype=0` (Столбец Result, строка CRC-8/MAXIM, сумма 0xA8. hex - hex)
data = [0x31, 0x00, 0x06]
crc = crc8(data, 0)
print(hex(crc))  # Вернет 0xa8.

data = [0x31, 0x01, 0x06]
crc = crc8(data, 0)
print(hex(crc))  # Вернет 0x6c.

data = [0x3e, 0x00, 0x06, 0xe4, 0x5c, 0x3e, 0x00, 0x00]
crc = crc8(data, 0)
print(hex(crc))  # Вернет  0xd2


def connectToPort(port='COM1'):
    """ Подключение к порту """
    try:
        ser.port = port
        ser.open()
        time.sleep(1)   # Ожидание первого сообщения
        print(f'Connect to {port}')

        while True:
            getLLS('31 00 06 A8')

            while ser.in_waiting > 0:
                data = ser.readline()
                parsLLS(data)

            time.sleep(2)

        return (True, f"Подключено к {ser.name}")

    except serial.SerialException as e:
        return print(False, f"Ошибка подключения к {ser.name}.\n. Err: {e}")


connectToPort("COM5")


# Функция подсчета контрольной суммы
# pass


# Перехваченные данные между Мастером и Рабом (Для примера)
#  С Rfid картой
"""
31 01 06 6C - это не HEX формат!  Вот HEX 0x31 0x01 0x06
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

# Запрос через пайтон (pyserial)
"""
GET: 310006A8
RESPONSE: ['3e', '00', '06', 'e4', '5c', '3e', '00', '00', 'd2'] # с картой  
GET: 310006A8
RESPONSE: ['3e', '00', '06', '00', '00', '00', '00', '00', 'f7'] # без карты
"""