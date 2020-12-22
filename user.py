import socket

port = 3000

c = socket.socket()

c.connect(('localhost',port))

name = input('enter your name')
c.send(bytes(name,'utf-8'))




# import socket
# import sys
# import time

# x=socket.socket()
# h_name = input(str("Enter the hostname of the server "))
# port = 8080

# x.connect((h_name,port))
# print("Connected to chat server")

while True: 
   incoming_message = c.recv(1024).decode()
   print(" Server :", incoming_message)
   message= input(str(">>"))
   Message = message.encode()
   c.send(message)
   print(" message has been sent...")