import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input('inserire indirizzo ip:')
port = int(input('inserire la porta:'))

serversocket.bind((host,port))

serversocket.listen(100)

clientsocket, addr = serversocket.accept()

i = 2

while True:
  if i == 2:
    a = input('inserisci il messaggio:')
    b = a.encode()
    clientsocket.send(b)
    i = i-1

  else:
    mr = clientsocket.recv(1024)
    print(mr.decode())
    i = i+1
