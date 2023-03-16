import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((socket.gethostname(), 1222))
conn.listen(5)

conn, address = conn.accept()
print("Connection from:" + str(address))
while True:
   data = conn.recv(1024).decode()
   if not data:
      break
   print("from connected user:" + str(data))
   data = input('->')
   conn.send(data.encode())
   
conn.close()
