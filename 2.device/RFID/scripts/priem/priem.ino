// Пример отправки и приёма структуры через Serial
// ПРИЁМНИК
// Ардуины соединены так:
// приёмник D10 -> отправитель D11

// структура для приёма
// должна соответствовать отпраляемой
struct Str {
  byte pref;
  byte adr;
  byte code;
  byte sum;
};

// создаём саму структуру
Str buf;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // читаем родным методом readBytes()
  // указываем ему буфер-структуру, но приводим тип к byte*
  // размер можно указать через sizeof()
  if (Serial.readBytes((byte*)&buf, sizeof(buf))) {
    Serial.println(buf.pref);
    Serial.println(buf.adr);
    Serial.println(buf.code);
    Serial.println(buf.sum);
  }
}
