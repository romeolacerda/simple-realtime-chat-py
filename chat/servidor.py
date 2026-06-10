import socket
import threading

HOST = '127.0.0.1'
PORT = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

roooms = {}

def broadcast(room, message):
    for i in roooms[room]:
        if isinstance(message, str):
            message = message.encode()

        i.send(message)

def enviarMensagem(name, room, client):
    while True:
        message = client.recv(1024)
        message = f"{name}: {message.decode()}\n"
        broadcast(room, message)

while True:
    client, addr = server.accept()
    client.send(b'SALA')
    room = client.recv(1024).decode()
    name = client.recv(1024).decode()
    if room not in roooms.keys():
        roooms[room] = []
    roooms[room].append(client)
    print(f'{name} se conectou na sala {room}! INFO {addr}')
    broadcast(room, f'{name}: Entrou na sala!\n')
    thread = threading.Thread(target=enviarMensagem, args=(name, room, client))
    thread.start()