from mfrc522 import MFRC522
import time

# CS == SDA
rdr = MFRC522(sck = 6, mosi = 5, miso = 3, rst = 1, cs = 7)

while True:
    cardValue = rdr.getCardValue()
    if cardValue != "":
        print(cardValue)
        address = 0
        
        while address < 64:
            print(address, ":", rdr.read(address))
            address += 1
        
    time.sleep(1)
