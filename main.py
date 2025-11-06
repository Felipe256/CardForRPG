def web_page():
  
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
  <label for="name">Nome (0-20):</label>
  <input type="text" maxlength="20" id="name" name="name"/>
  <br>
  <label for="origem">Origem (0-99):</label>
  <input type="number" min="0" max="99" id="origem" name="origem"/>
  <br>
  <label for="classe">Classe (0-25):</label>
  <input type="number" min="0" max="25" id="classe" name="classe"/>
  <br>
  <label for="PV">PV atual (0-300):</label>
  <input type="number" min="0" max="300" id="PV" name="PV"/>
  <br>
  <label for="PVmax">PV Max (0-300):</label>
  <input type="number" min="0" max="300" id="PVmax" name="PVmax"/>
  <br>
  <label for="SAN">SAN atual (0-200):</label>
  <input type="number" min="0" max="200" id="SAN" name="SAN">
  <br>
  <label for="SAN">SAN max (0-200):</label>
  <input type="number" min="0" max="200" id="SANmax" name="SANmax">
  <br>
  <label for="PE">PE atual (0-250):</label>
  <input type="number" min="0" max="250" id="PE" name="PE">
  <br>
  <label for="PEmax">PE max (0-250):</label>
  <input type="number" min="0" max="250" id="PEmax" name="PEmax">
  <br>
  <label for="COND">condicao (max 5 entre virgulas sem espaco):</label>
  <input type="text" maxlength="14" id="COND" name="COND">
  <br>
  <label for="DEF">Defesa (1-50):</label>
  <input type="number" min="1" max="50" id="DEF" name="DEF">
  <br>
  <label for="ESQ">Esquiva (1-99):</label>
  <input type="number" min="1" max="99" id="ESQ" name="ESQ">
  <br>
  <label for="BLQ">Bloqueio (1-50):</label>
  <input type="number" min="1" max="50" id="BLQ" name="BLQ">
  <br>
  <label for="CAR">Carga (1-99):</label>
  <input type="number" min="1" max="99" id="CAR" name="CAR">
  <br>
  <label for="CARmax">Carga max (1-99):</label>
  <input type="number" min="1" max="99" id="CARmax" name="CARmax">
  <br>
  <input type="submit">
  </form>
  <p><a href="/?mode=read"><button class="button">READ</button></a></p>
  <p><a href="/?mode=write"><button class="button button2">WRITE</button></a></p>
  </body></html>"""
    
  return html


port = 89
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
  
  if formRead == 7:
    block = int(request.split("block=")[1].replace("'", ""))
    print("Lendo bloco ", block)
    readCard(readingNum = block)
    
  if formWrite == 7:
    resposta = request.split("\\r\\n\\r\\n")
    resposta.pop(0)
    print("RESPOSTA AKI: ", resposta[0].split("&"))
    
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()