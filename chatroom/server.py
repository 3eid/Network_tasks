from socket import *
from threading import Thread

host = '127.0.0.1'
port = 8888

clients = []
nicknames = []

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(3)

def broadcast(message,sender=None):
    for client in clients:
        if sender and client is sender:
          continue  
        client.send(message)

def handle_client(conn):
    while True:
        try:
            message = conn.recv(1024)
            broadcast(message,conn)
        except Exception as e:
            index = clients.index(conn)
            nickname = nicknames.pop(index)
            clients.remove(conn)
            conn.close()
            broadcast(f"{nickname} left!".encode())
            break


while True:
    conn, addr = server_socket.accept()
    conn.send("NICK".encode())
    nickname = conn.recv(1024).decode()
    clients.append(conn)
    nicknames.append(nickname)
    broadcast(f"{nickname} joined the room!".encode())
    client_thread = Thread(target=handle_client, args=(conn,),)
    client_thread.start()