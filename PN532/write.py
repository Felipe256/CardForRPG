import time
from machine import Pin, SPI
import PN532 as nfc

# Configura SPI
try:
    spi = SPI(1, baudrate=100000, polarity=0, phase=0, sck=Pin(4), mosi=Pin(6), miso=Pin(5))
    print("SPI inicializado com sucesso!")
except Exception as e:
    print("Erro ao inicializar SPI:", e)

cs = Pin(7, Pin.OUT)
cs.value(1)
time.sleep(0.1)

# Inicializa PN532
try:
    pn532 = nfc.PN532(spi, cs)
    ic, ver, rev, support = pn532.get_firmware_version()
    print('PN532 encontrado! Versão do firmware: {0}.{1}'.format(ver, rev))
except Exception as e:
    print("Erro ao inicializar PN532:", e)

# Configura para cartões MIFARE
pn532.SAM_configuration()

# Chave padrão MIFARE
key = bytearray([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])  # Chave A

print('Aproxime o cartão para escrever...')
uid = pn532.read_passive_target(timeout=1.0)
if uid is None:
    print('Nenhum cartão detectado!')
else:
    print('Cartão encontrado! UID:', [hex(i) for i in uid])
    
    # Autentica no bloco 4
    try:
        if pn532.mifare_classic_authenticate_block(uid, 4, nfc.MIFARE_CMD_AUTH_A, key):
            # Dados a escrever (16 bytes exatos)
            dados = bytearray(b'Ola do ESP32-C3!')  # 16 bytes, sem acento
            print('Tamanho dos dados:', len(dados))  # Debug
            if pn532.mifare_classic_write_block(4, dados):
                print('Escrita bem-sucedida no bloco 4!')
            else:
                print('Erro ao escrever no bloco 4!')
        else:
            print('Falha na autenticação! Verifique a chave ou o cartão.')
    except Exception as e:
        print("Erro na autenticação:", e)