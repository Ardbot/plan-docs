#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9          // Пин для сброса модуля RC522
#define SS_PIN 10          // Пин для выбора Slave (NSS)

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Создаем объект MFRC522

void setup() {
  Serial.begin(9600);           // Начинаем сериал связь
  SPI.begin();                  // Инициализируем SPI библиотеку
  mfrc522.PCD_Init();           // Инициализируем модуль RC522
  Serial.println("Ready to read RFID cards!");
}

void loop() {

  // Ждем, пока в буфере последовательного порта появятся не менее 4 байт данных
  while (Serial.available() < 4) {
    // Подождем
  }

  // Чтение 4 байт из буфера последовательного порта
  uint32_t data;
  Serial.readBytes((char*)&data, 4);
  Serial.println(3100066C,HEX);
}

//  
//  // Ищем карты
//  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
//    // Печатаем серийный номер карты
//    Serial.print("Card UID: ");
//    for (byte i = 0; i < mfrc522.uid.size; ++i) {
//      Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
//      Serial.print(mfrc522.uid.uidByte[i], HEX);
//    }
//    Serial.println();
//    mfrc522.PICC_HaltA();  // Останавливаем карту
//  }
//  
//  //  Читаем входящие данные с ведущего устройства.
//  if (Serial.available() > 0) {
//    // Чтение данных из буфера и вывод на последовательный порт
//    char data = Serial.read();
//    Serial.print("Прочитано: ");
//    Serial.println(data);
//  }
//}
