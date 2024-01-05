// Пример отправки и приёма структуры через Serial
// ОТПРАВИТЕЛЬ
// Ардуины соединены так:
// отправитель D11 -> приёмник D10
//#include <SoftwareSerial.h>
//SoftwareSerial mySerial(10, 11); // RX, TX

struct Str {
  byte pref;
  byte adr;
  byte code;
};

void setup() {
  Serial.begin(9600);
//  mySerial.begin(4000);
}

void loop() {
  // буфер на отправку
  Str buf;

  // заполняем
  buf.pref = 49;
  buf.adr = 1;
  buf.code = 6;

  // отправляем родным write()
  // указываем ему буфер-структуру, но приводим тип к byte*
  // размер можно указать через sizeof()
  Serial.write((byte*)&buf, sizeof(buf));
  delay(2000);
}
