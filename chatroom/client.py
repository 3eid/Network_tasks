from socket import *
from threading import Thread

host = '127.0.0.1'
port = 8888

nickname = input("Enter your nickname: ")

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))

def handle_rcv():
    while True:
        message = client_socket.recv(1024).decode()
        try:
            if message == "NICK":
                client_socket.send(nickname.encode())
            else:
                print(message)
        except:
            print("An Error Occured")
            client_socket.close()
            break
        
def handle_send():
    while True:
        message = f"{nickname}: {input()}"
        client_socket.send(message.encode())

write_thread = Thread(target=handle_rcv)
read_thread = Thread(target=handle_send)

write_thread.start()
read_thread.start()