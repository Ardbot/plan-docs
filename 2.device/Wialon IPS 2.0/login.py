# Пакет логина

import crcmod


def calculate_crc16(data):
    crc16 = crcmod.predefined.Crc('crc-16')
    crc16.update(data.encode('utf-8'))
    return crc16.hexdigest().upper()


def create_login_packet(protocol_version, imei, password):
    packet = f"#L#{protocol_version};{imei};{password};"
    crc = calculate_crc16(packet)
    return f"{packet}{crc}\r\n"


def parse_login_response(response):
    response_parts = response.split('#')
    if response_parts[1] == "AL":
        return response_parts[2]
    return None


# Пример использования:
protocol_version = "2.0"
imei = "123456789012345"
password = "your_password"

login_packet = create_login_packet(protocol_version, imei, password)
print(f"Login Packet: {login_packet}")

# Здесь вы отправляете login_packet на сервер и получаете ответ
server_response = "#AL#1\r\n"  # Пример успешного ответа
parsed_response = parse_login_response(server_response)

if parsed_response == "1":
    print("Авторизация прошла успешно")
elif parsed_response == "0":
    print("Сервер отклонил подключение")
elif parsed_response == "01":
    print("Ошибка проверки пароля")
elif parsed_response == "10":
    print("Ошибка проверки контрольной суммы")
else:
    print("Некорректный ответ сервера")
