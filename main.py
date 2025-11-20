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
  
  
  html = """<html><head> <title>Card For RPG</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1>
  <form action="/?formRead" method="POST">
  <label for="block">Block of Character (0-64):</label><input type="number" id="block" name="block" min="0" max="64"/>
  <input type="submit">
  </form>
  
  <form action="/?formWrite" method="POST">
  <label for="name">Nome (0-16):</label>
  <input type="text" maxlength="16" value='""" + nome + """' id="name" name="name"/>
  <br>
  <label for="origem">Origem (0-99):</label>
  <input type="number" min="0" max="99" value=""" + str(origem) + """ id="origem" name="origem"/>
  <br>
  <label for="classe">Classe (0-25):</label>
  <input type="number" min="0" max="25" value=""" + str(classe) + """ id="classe" name="classe"/>
  <br>
  <label for="PV">PV atual (0-300):</label>
  <input type="number" min="0" max="300" value=""" + str(pvAtual) + """ id="PV" name="PV"/>
  <br>
  <label for="PVmax">PV Max (0-300):</label>
  <input type="number" min="0" max="300" value=""" + str(pvMax) + """ id="PVmax" name="PVmax"/>
  <br>
  <label for="SAN">SAN atual (0-200):</label>
  <input type="number" min="0" max="200" value=""" + str(sanAtual) + """ id="SAN" name="SAN">
  <br>
  <label for="SAN">SAN max (0-200):</label>
  <input type="number" min="0" max="200" value=""" + str(sanMax) + """ id="SANmax" name="SANmax">
  <br>
  <label for="PE">PE atual (0-250):</label>
  <input type="number" min="0" max="250" value=""" + str(peAtual) + """ id="PE" name="PE">
  <br>
  <label for="PEmax">PE max (0-250):</label>
  <input type="number" min="0" max="250" value=""" + str(peMax) + """ id="PEmax" name="PEmax">
  <br>
  <label for="COND">condicao (max 5 entre espaco):</label>
  <input type="text" maxlength="14" value=""" + str(condicao) + """ id="COND" name="COND">
  <br>
  <label for="DEF">Defesa (1-50):</label>
  <input type="number" min="1" max="50" value=""" + str(defesa) + """ id="DEF" name="DEF">
  <br>
  <label for="ESQ">Esquiva (1-99):</label>
  <input type="number" min="1" max="99" value=""" + str(esquiva) + """ id="ESQ" name="ESQ">
  <br>
  <label for="BLQ">Bloqueio (1-50):</label>
  <input type="number" min="1" max="50" value=""" + str(bloqueio) + """ id="BLQ" name="BLQ">
  <br>
  <label for="CAR">Carga (1-99):</label>
  <input type="number" min="1" max="99" value=""" + str(carga) + """ id="CAR" name="CAR">
  <br>
  <label for="CARmax">Carga max (1-99):</label>
  <input type="number" min="1" max="99" value=""" + str(cargaMax) + """ id="CARmax" name="CARmax">
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
    
  if formWrite == 7:
    resposta = request.split("\\r\\n\\r\\n")
    resposta.pop(0)
    resposta = resposta[0].split("&")
    paraEscrever = []
    for elemento in resposta:
        paraEscrever.append(elemento.split("=")[1].replace("'", ""))
    writeCard()
    #bloco 4 = nome(16)
    writeCard(writingNum = 4, data = paraEscrever[0])
    #bloco 5 = origem(2), classe(2), pv atual (3), pv max(3)
    dataBloco5 = paraEscrever[1]+","+paraEscrever[2]+","+paraEscrever[3]+","+paraEscrever[4]
    writeCard(writingNum = 5, data = dataBloco5)
    #bloco 6 = san atual(3), san max(3), pe atual(3), pe max(3)
    dataBloco6 = paraEscrever[5]+","+paraEscrever[6]+","+paraEscrever[7]+","+paraEscrever[8]
    writeCard(writingNum = 6, data = dataBloco6)
    #bloco 8 = condicao
    dataBloco8 = paraEscrever[9]
    writeCard(writingNum = 8, data = dataBloco8)
    #bloco 9 = defesa(2), esquiva(2), bloqueio(2), carga(2), carga max(2)
    dataBloco9 = paraEscrever[10]+","+paraEscrever[11]+","+paraEscrever[12]+","+paraEscrever[13]+","+paraEscrever[14]
    writeCard(writingNum = 9, data = dataBloco9)
  
  if resetButton == 6:
    Bnome = ""
    Borigem = 0
    Bclasse = 0
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
    
    
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()