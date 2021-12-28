import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port=1234
serverSocket.bind(('', port))
print("Server listening on port "+ str(port))
while True:
    message, address = serverSocket.recvfrom(1024)
    print(message)