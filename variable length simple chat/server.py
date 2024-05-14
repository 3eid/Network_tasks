from socket import *

# Initialize a TCP/IP socket
server_socket = socket(AF_INET, SOCK_STREAM)

host = '127.0.0.1'
port = 8888

# Bind the socket to the host and port
server_socket.bind((host, port))
#configure listening and backlog
server_socket.listen(5)

# Accept an incoming connection
client_socket, client_address = server_socket.accept()
print(f"[*] Connection established with {client_address}")

while True:
    # Receive the length of the incoming message (fixed size: 10 bytes)
    length_bytes = client_socket.recv(10)
    message_length = int(length_bytes.decode('utf-8'))

    # Receive the actual message based on the length received
    message = client_socket.recv(message_length).decode('utf-8')
    
    if message == "q":
        print("End of Connection")
        client_socket.close()
        break
    
    print("Client:", message)

    # Get server's response from user input
    response = input('Server: ')
    

    # Send the length of the response (fixed size: 10 bytes)
    response_bytes = response.encode('utf-8')
    response_length = str(len(response_bytes)).zfill(10).encode('utf-8')
    client_socket.send(response_length)

    # Send the actual response
    client_socket.send(response_bytes)
    if response == 'q':
            print('[*] Connection closing, goodbye!')
            client_socket.close()
            break
        
# Close the server socket
server_socket.close()
