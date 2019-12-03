import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)

sock.connect(('localhost', 9090))
print('Соединение с сервером.')

msg = input()
print('Отправка данных серверу.')
#msg = "Hi!"
sock.send(msg.encode())

print('Прием данных от сервера.')
data = sock.recv(1024)
print('Разрыв соединения с сервером.')
sock.close()

print(data.decode())
