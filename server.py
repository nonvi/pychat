import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input('inserire indirizzo ip:')
port = int(input('inserire la porta:'))
nickname = input('seleziona nickname:')



serversocket.bind((host,port))


serversocket.listen(2)


clientsocket, addr = serversocket.accept()

i = 2

while True:
  if i == 2:
    a = input('inserisci il messaggio:')
    b = a.encode()
    c = nickname.encode()
    clientsocket.send(c + b':' + b)
    i = i-1

  else:
    mr = clientsocket.recv(1024)
    print(mr.decode())
    i = i+1
