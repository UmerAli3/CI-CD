import socket
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


c.connect(('127.0.0.1',12345))
c.sendall("hello server ".encode())   
data = c.recv(1024).decode()
print ("recieved",data)
c.close()