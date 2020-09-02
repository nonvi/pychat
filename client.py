import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input('inserire indirizzo ip:')
port = int(input('inserire la porta:'))

s.connect((host,port))

i = 1


while True:
  if i == 2:
    a = input('inserisci il messagio:')
    b = a.encode()
    s.send(b)
    i = i-1

  else:
    tm = s.recv(1024)
    print(tm.decode())
    i = i+1
  
