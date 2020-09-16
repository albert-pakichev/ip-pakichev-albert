from socket import*
import time
#
# s = socket(AF_INET, SOCK_STREAM) #Создает сокет ТСР
# s.bind(("",8888)) # присваивает порт 888
# s.listen(5) # Переходит в режим ожидания запросов,
# # одновременно обслуживает не более 5 запрососв
#
#
# while True:
#     client, addr = s.accept() #Принять запрос на соединение
#     print("Получен запрос на соединение от %s" % str(addr))
#     timestr = time.ctime(time.time()) + "\n"
#     client.send(timestr.encode('ascii'))
#     client.close()


import time
import socket


#Настройки хоста и порта
host = 'localhost'
port = 9090
# Список подключенных клиентов
clients = []

# создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
quit = False
print("[ Server Started ]")
# создаем сокет
while not quit:
    try:
        # принимаем данные с клиентов: данные, адрес клиента
        data, addr = s.recvfrom(1024)

        #если клиент "новый", добавляем его в наш список
        if addr not in clients:
            clients.append(addr)
        #текущее время
        itsatime = time.strtime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
        print(data.decode("utf-8"))
        for client in clients:
            if addr != client:
                s.sendto(data,client)
    except Exception as ex:
        print(ex)
        print("\n[ Server Stoppped ]")
        quit = True
#Не забываем закрывать сокет
s.close()