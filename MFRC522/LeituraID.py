from machine import Pin, SPI
import mfrc522
import time

# Configura SPI no ESP32-C3
spi = SPI(
    1,
    baudrate=1000000,
    polarity=0,
    phase=0,
    sck=Pin(9),
    mosi=Pin(8),
    miso=Pin(7)
)

# Define CS e RST
rdr = mfrc522.MFRC522(spi=spi, gpioRst=Pin(5), gpioCs=Pin(10))

print("Aproxime o cartão/tag...")

while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = "%02X%02X%02X%02X" % tuple(raw_uid)
            print("UID do cartão:", uid)
    time.sleep(0.5)
