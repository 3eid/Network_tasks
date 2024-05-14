from socket import *

# Initialize a TCP/IP socket
client_socket = socket(AF_INET, SOCK_STREAM)
print("[*] Socket successfully created")

server_host = '127.0.0.1'
server_port = 8888

# Connect to the server
client_socket.connect((server_host, server_port))

while True:
    # Get client's message from user input
    client_message = input('Client: ')


    # Send the length of the message (fixed size: 10 bytes)
    message_data = client_message.encode('utf-8')
    message_length = str(len(message_data)).zfill(10).encode('utf-8')
    client_socket.send(message_length)

    # Send the actual message
    client_socket.send(message_data)
    if client_message == 'q':
        print('[*] Connection closing, goodbye!')
        client_socket.close()
        break

    # Receive the length of the server's response (fixed size: 10 bytes)
    length_bytes = client_socket.recv(10)
    response_length = int(length_bytes.decode('utf-8'))

    # Receive the server's response based on the length received
    server_message = client_socket.recv(response_length).decode('utf-8')
    if server_message == "q":
        client_socket.close()
        print("Server:", server_message)
        break
    

# Close the client socket
client_socket.close()
