def web_page():
  
  
  
  nome = Bnome
  origem = Borigem
  classe = Bclasse
  pvAtual = BpvAtual
  pvMax = BpvMax
  sanAtual = BsanAtual
  sanMax = BsanMax
  peAtual = BpeAtual
  peMax = BpeMax
  condicao = Bcondicao
  defesa = Bdefesa
  esquiva = Besquiva
  bloqueio = Bbloqueio
  carga = Bcarga
  cargaMax = BcargaMax
  
  nex = Bnex
  forca = Bforca
  agilidade = Bagilidade
  intelecto = Bintelecto
  vigor = Bvigor
  presenca = Bpresenca
  
  fortitude = Bfortitude
  reflexo = Breflexo
  
  
  html = """<html><head> <title>Card For RPG</title> <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1>
  <form action="/?formRead" method="POST">
  <input type="submit" value ="Ler cartão">
  </form>
  
  <form action="/?formWrite" method="POST">
  <label for="name">Nome (0-16):</label>
  <input type="text" maxlength="16" value='""" + nome + """' id="name" name="name"/>
  <br>
  <label for="origem">Origem (0-99):</label>
  <input type="number" min="0" max="99" value=""" + str(origem) + """ id="origem" name="origem"/>
  <br>
  <label for="classe">Classe (1-15):</label>
  <input type="number" min="1" max="15" value=""" + str(classe) + """ id="classe" name="classe"/>
  <br>
  <label for="PV">PV atual (0-300):</label>
  <input type="number" min="0" max="300" value=""" + str(pvAtual) + """ id="PV" name="PV"/>
  <br>
  <label for="PVmax">PV Max (0-300):</label>
  <input type="number" min="0" max="300" value=""" + str(pvMax) + """ id="PVmax" name="PVmax" readonly/>
  <br>
  <label for="SAN">SAN atual (0-200):</label>
  <input type="number" min="0" max="200" value=""" + str(sanAtual) + """ id="SAN" name="SAN">
  <br>
  <label for="SAN">SAN max (0-200):</label>
  <input type="number" min="0" max="200" value=""" + str(sanMax) + """ id="SANmax" name="SANmax" readonly>
  <br>
  <label for="PE">PE atual (0-250):</label>
  <input type="number" min="0" max="250" value=""" + str(peAtual) + """ id="PE" name="PE">
  <br>
  <label for="PEmax">PE max (0-250):</label>
  <input type="number" min="0" max="250" value=""" + str(peMax) + """ id="PEmax" name="PEmax" readonly>
  <br>
  <label for="COND">condição (max 5 entre espaco):</label>
  <input type="text" maxlength="14" value=""" + str(condicao) + """ id="COND" name="COND">
  <br>
  <label for="DEF">Defesa (1-50):</label>
  <input type="number" min="1" max="50" value=""" + str(defesa) + """ id="DEF" name="DEF" readonly>
  <br>
  <label for="ESQ">Esquiva (1-99):</label>
  <input type="number" min="1" max="99" value=""" + str(esquiva) + """ id="ESQ" name="ESQ" readonly>
  <br>
  <label for="BLQ">Bloqueio (1-50):</label>
  <input type="number" min="1" max="50" value=""" + str(bloqueio) + """ id="BLQ" name="BLQ" readonly>
  <br>
  <label for="CAR">Carga (1-99):</label>
  <input type="number" min="1" max="99" value=""" + str(carga) + """ id="CAR" name="CAR">
  <br>
  <label for="CARmax">Carga max (1-99):</label>
  <input type="number" min="1" max="99" value=""" + str(cargaMax) + """ id="CARmax" name="CARmax" readonly>
  <br>
  <label for="NEX">NEX (1-20):</label>
  <input type="number" min="1" max="20" value=""" + str(nex) + """ id="NEX" name="NEX">
  <br>
  <label for="FOR">Força (0-9):</label>
  <input type="number" min="0" max="9" value=""" + str(forca) + """ id="FOR" name="FOR">
  <br>
  <label for="AGI">Agilidade (0-9):</label>
  <input type="number" min="0" max="9" value=""" + str(agilidade) + """ id="AGI" name="AGI">
  <br>
  <label for="INT">Intelecto (0-9):</label>
  <input type="number" min="0" max="9" value=""" + str(intelecto) + """ id="INT" name="INT">
  <br>
  <label for="VIG">Vigor (0-9):</label>
  <input type="number" min="0" max="9" value=""" + str(vigor) + """ id="VIG" name="VIG">
  <br>
  <label for="PRE">Presença (0-9):</label>
  <input type="number" min="0" max="9" value=""" + str(presenca) + """ id="PRE" name="PRE">
  <br>
  <label for="FOR">Fortitude (0-3):</label>
  <input type="number" min="0" max="3" value=""" + str(fortitude) + """ id="FOR" name="FOR">
  <br>
  <label for="REF">Reflexo (0-3):</label>
  <input type="number" min="0" max="3" value=""" + str(reflexo) + """ id="REF" name="REF">
  <br>
  <input type="submit">
  </form>
  <p><a href="/?reset"><button class="button">RESET</button></a></p>
  <p><a href="/?mode=write"><button class="button button2">WRITE</button></a></p>
  </body></html>"""
    
  return html


port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(5)

print("Server stablish on port ", port)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  formRead = request.find('/?formRead')
  formWrite = request.find('/?formWrite')
  resetButton = request.find('/?reset')
  
  if formRead == 7:
    
    Bnome = readCard(readingNum = 4).replace(" ", "")
    
    dataBloco5 = readCard(readingNum = 5).replace(" ", "")
    dataBloco5 = dataBloco5.split(",")
    Borigem = int(dataBloco5[0])
    Bclasse = int(dataBloco5[1])
    BpvAtual = int(dataBloco5[2])
    BpvMax = int(dataBloco5[3])
    
    dataBloco6 = readCard(readingNum = 6).replace(" ", "")
    dataBloco6 = dataBloco6.split(",")
    BsanAtual = int(dataBloco6[0])
    BsanMax = int(dataBloco6[1])
    BpeAtual = int(dataBloco6[2])
    BpeMax = int(dataBloco6[3])
    
    dataBloco8 = readCard(readingNum = 8).replace("+", " ")
    Bcondicao = dataBloco8
    
    dataBloco9 = readCard(readingNum = 9).replace(" ", "")
    dataBloco9 = dataBloco9.split(",")
    Bdefesa = dataBloco9[0]
    Besquiva = dataBloco9[1]
    Bbloqueio = dataBloco9[2]
    Bcarga = dataBloco9[3]
    BcargaMax = dataBloco9[4]
    
    dataBloco10 = readCard(readingNum = 10).replace(" ", "")
    dataBloco10 = dataBloco10.split(",")
    Bnex = dataBloco10[0]
    Bforca = dataBloco10[1]
    Bagilidade = dataBloco10[2]
    Bintelecto = dataBloco10[3]
    Bvigor = dataBloco10[4]
    Bpresenca = dataBloco10[5]
    
    dataBloco12 = readCard(readingNum = 12).replace(" ", "")
    dataBloco12 = dataBloco12.split(",")
    Bfortitude = dataBloco12[0]
    Breflexo = dataBloco12[1]
    
  if formWrite == 7:
    resposta = request.split("\\r\\n\\r\\n")
    resposta.pop(0)
    resposta = resposta[0].split("&")
    paraEscrever = []
    for elemento in resposta:
        paraEscrever.append(elemento.split("=")[1].replace("'", ""))
        
    clas = int(paraEscrever[2])
    
    nx = int(paraEscrever[15])
    forc = int(paraEscrever[16])
    agi = int(paraEscrever[17])
    intel = int(paraEscrever[18])
    vigo = int(paraEscrever[19])
    pres = int(paraEscrever[20])
    
    pvM = 0
    sanM = 0
    peM = 0
    if (clas - 1) // 5 == 0: #combatente
        pvM = 20 + 5 * (nx - 1) + vigo * nx
        sanM = 12 + 3*(nx - 1)
        peM = nx * (pres + 2)
    elif (clas - 1) // 5 == 1: #especialista
        pvM = 16 + 4 * (nx - 1) + vigo * nx
        sanM = 16 + 4 * (nx - 1)
        peM = nx * (pres + 3)
    else: #ocultista
        pvM = 12 + 3 * (nx - 1) + vigo * nx
        sanM = 20 + 5 * (nx - 1)
        peM = nx * (pres + 4)
    
    cargaM = 2
    if forc != 0:
        cargaM = 5 * forc
    if (clas - 1) == 9: # especialista tecnico
        cargaM = (forc + intel) * 5
    
    #pericias (0 - 1 - 2 - 3) -> (0 - 5 - 10 - 15)
    fort = int(paraEscrever[21])
    ref = int(paraEscrever[22])
    
    defe = agi + 10
    esq = defe + ref * 5
    
    bloq = fort * 5
    
    
    #bloco 4 = nome(16)
    writeCard(writingNum = 4, data = paraEscrever[0])
    
    #bloco 5 = origem(2), classe(2), pv atual (3), pv max(3)
    dataBloco5 = paraEscrever[1]+","+str(clas)+","+paraEscrever[3]+","+str(pvM)
    writeCard(writingNum = 5, data = dataBloco5)
    
    #bloco 6 = san atual(3), san max(3), pe atual(3), pe max(3)
    dataBloco6 = paraEscrever[5]+","+str(sanM)+","+paraEscrever[7]+","+str(peM)
    writeCard(writingNum = 6, data = dataBloco6)
    
    #bloco 8 = condicao
    dataBloco8 = paraEscrever[9]
    writeCard(writingNum = 8, data = dataBloco8)
    
    #bloco 9 = defesa(2), esquiva(2), bloqueio(2), carga(2), carga max(2)
    dataBloco9 = str(defe)+","+ str(esq) +","+str(bloq)+","+paraEscrever[13]+","+str(cargaM)
    writeCard(writingNum = 9, data = dataBloco9)
    
    #bloco 10 = nex(1), forca(1), agilidade(1), intelecto(1), vigor(1), presença(1)
    dataBloco10 = str(nx)+","+str(forc)+","+str(agi)+","+str(intel)+","+str(vigo)+","+str(pres)
    writeCard(writingNum = 10, data = dataBloco10)
    
    #bloco 12 = fortitude(1), reflexo(1)
    dataBloco12 = str(fort)+","+str(ref)
    writeCard(writingNum = 12, data = dataBloco12)
  
  if resetButton == 6:
    Bnome = ""
    Borigem = 0
    Bclasse = 1
    BpvAtual = 0
    BpvMax = 0
    BsanAtual = 0
    BsanMax = 0
    BpeAtual = 0
    BpeMax = 0
    Bcondicao = "0 0 0 0 0"
    Bdefesa = 0
    Besquiva = 0
    Bbloqueio = 0
    Bcarga = 0
    BcargaMax = 0
    
    Bnex = 1
    Bforca = 0
    Bagilidade = 0
    Bintelecto = 0
    Bvigor = 0
    Bpresenca = 0

    Bfortitude = 0
    Breflexo = 0
    
    
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()