try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Galaxy M31A960 2G'
password = 'Felipe2004'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

print("Trying to connect to ", ssid, " with password ", password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

def readCard(readingNum = 4):
    import time
    from machine import Pin, SPI
    import PN532 as nfc

    try:
        spi = SPI(1, baudrate=100000, polarity=0, phase=0, sck=Pin(4), mosi=Pin(6), miso=Pin(5))
        print("SPI inicializado com sucesso!")
    except Exception as e:
        print("Erro ao inicializar SPI:", e)

    cs = Pin(7, Pin.OUT)
    cs.value(1)
    time.sleep(2.0)

    for _ in range(5):
        try:
            pn532 = nfc.PN532(spi, cs)
            ic, ver, rev, support = pn532.get_firmware_version()
            print('PN532 encontrado! Versão do firmware: {0}.{1}'.format(ver, rev))
            break
        except Exception as e:
            print("Erro ao inicializar PN532:", e)
            time.sleep(0.5)
    else:
        print("Falha ao inicializar PN532 após 5 tentativas!")
        raise RuntimeError("Não foi possível inicializar o PN532")

    pn532.SAM_configuration()

    key = bytearray([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])

    print('Aproxime o cartão para ler...')
    while True:
        uid = pn532.read_passive_target(timeout=1.5)
        if uid is None:
            print('.', end='')
        else:
            print('\nCartão encontrado! UID:', [hex(i) for i in uid])
            try:
                auth_success = pn532.mifare_classic_authenticate_block(uid, readingNum, nfc.MIFARE_CMD_AUTH_A, key)
                print('Autenticação bem-sucedida:', auth_success)
                if auth_success:
                    time.sleep(0.2)
                    dados = pn532.mifare_classic_read_block(readingNum)
                    print('Resposta da leitura:', [hex(i) for i in dados])
                    if dados:
                        try:
                            print('Dados no bloco ',readingNum,':', dados.decode('utf-8').rstrip('\x00'))
                            break
                        except Exception as e:
                            print('Falha na decodificação!')
                    else:
                        print('Erro ao ler o bloco ', readingNum,'!')
                else:
                    print('Falha na autenticação!')
            except Exception as e:
                print("Erro na leitura:", e)
        time.sleep(1.5)

    