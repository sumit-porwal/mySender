import socket

s = socket.socket()
print('socket created')

s.bind(('localhost',3000))

s.listen(2)
print('listening for connection....')

while True:
    c,addr = s.accept();
    name = c.recv(1024).decode()
    print('connected with', addr,name )

    c.send(bytes('you are connected','utf-8'))
    c.close()



