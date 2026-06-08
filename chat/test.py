import socket

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

mensagem = client.recv(1024)
if mensagem == b'SALA':
    client.send(b'Jogos')
    client.send(b'Caio')