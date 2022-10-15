# codigo para verificar portas abertas 

import socket

url = 'bancocn.com'
porta = [21,22,80,443,445,3306,25]

for port in porta:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1.5)
    code  = client.connect_ex((url, port))
    if code == 0:
        print(f"|{port}| aberta")
    else:
        print(f"|{port}| fechada")

#client.send(b"hello word")
#resposta = client.recv(1024)
#print(resposta.decode())