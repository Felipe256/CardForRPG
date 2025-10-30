import time
from machine import Pin, SPI
import PN532 as nfc

# Configura SPI para ESP32-C3 (SPI2, pinos seguros)
try:
    spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=Pin(4), mosi=Pin(6), miso=Pin(5))
    print("SPI inicializado com sucesso!")
except Exception as e:
    print("Erro ao inicializar SPI:", e)

cs = Pin(7, Pin.OUT)
cs.value(1)  # CS alto

# Inicializa PN532
try:
    pn532 = nfc.PN532(spi, cs)
    ic, ver, rev, support = pn532.get_firmware_version()
    print('PN532 encontrado! Versão do firmware: {0}.{1}'.format(ver, rev))
except Exception as e:
    print("Erro ao inicializar PN532:", e)

# Configura para cartões MIFARE
pn532.SAM_configuration()

print('Aproxime um cartão NFC...')
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is None:
        print('.', end='')
    else:
        print('\nCartão encontrado! UID: ', [hex(i) for i in uid])
        string_uid = '-'.join([str(i) for i in uid])
        print('UID como número: ' + string_uid)
    time.sleep(1)
