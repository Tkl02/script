import socket

url = 'bancocn.com'
porta = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(20)
code  = client.connect_ex((url, porta))

#client.send(b"hello word")
#resposta = client.recv(1024)
#print(resposta.decode())

print(code)