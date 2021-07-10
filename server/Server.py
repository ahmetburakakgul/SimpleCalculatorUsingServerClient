import socket

host = "0.0.0.0"
port = 4444
server = socket.socket()
server.bind((host, port))
server.listen(5)
print("Server Çalışıyor")


while(True):
    client, address = server.accept()
    print('Bağlanan Adres', address)
    while(True):
         try:
              problem=client.recv(1024).decode()#istemciden gelen,ara bellek boyutu 1024 olan byte tipindeki mesaj stringe dönüşür
              print("Problem:", problem)
              result=eval(problem)
              client.send(str(result).encode())
         except (Exception ):
               client.send("Hata".encode())

    client.close()
