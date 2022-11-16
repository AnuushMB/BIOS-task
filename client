import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),1222))

message = input(" -> ")  
while True:
    client_socket.send(message.encode())  
    data = client_socket.recv(1024).decode()  

    print('Received from server: ' + data)  

    message = input(" -> ")  
client_socket.close() 
