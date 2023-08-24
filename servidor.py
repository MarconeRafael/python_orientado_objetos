import socket 
HOST = '127.0.0.1'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando')
conn = s.accept()
ender = s.accept()
print('conectado em', ender)
while True:
     data = con.recv(1024)
     if not data:
          print('Fechando conexão')
          conn.close()
          break
     conn.sendall(data)