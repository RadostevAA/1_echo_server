import socket

sock = socket.socket()
print('Запуск сервера.')
sock.bind(('', 9090))
print('Прослушивание порта.')
sock.listen(0)

conn, addr = sock.accept()
print('Подключение клиента.')
print(addr)

msg = ''

while True:
    print('Прием данных от клиента.')
    data = conn.recv(1024)
    if not data:
        print('Отключение клиента.')
        break
    msg += data.decode()
    print('Отправка данных клиенту.')
    conn.send(data)
    

print(msg)
print('Остановка сервера.')
conn.close()
