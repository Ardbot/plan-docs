function crc8(data, crc) {
  for (let i = 0; i < data.length; i++) {
    let byte = data[i];
    let xor = byte ^ crc;
    crc = 0;
    if (xor & 0x01) {
      crc ^= 0x5e;
    }
    if (xor & 0x02) {
      crc ^= 0xbc;
    }
    if (xor & 0x04) {
      crc ^= 0x61;
    }
    if (xor & 0x08) {
      crc ^= 0xc2;
    }
    if (xor & 0x10) {
      crc ^= 0x9d;
    }
    if (xor & 0x20) {
      crc ^= 0x23;
    }
    if (xor & 0x40) {
      crc ^= 0x46;
    }
    if (xor & 0x80) {
      crc ^= 0x8c;
    }
  }

  return crc;
}

// Пример использования
let data = [0x31, 0x00, 0x06];
let crc = crc8(data, 0);
console.log(crc.toString(16)); // Выводит: "a8"