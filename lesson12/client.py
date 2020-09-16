# #Программа клиента, запрашивающего текущее время
# from socket import*
#
# s = socket(AF_INET, SOCK_STREAM) # Создать сокет ТСР
# s.connect(('localhost',8888)) #Соединиться с сервером
# tm = s.recv(1024) # Принять не более 1024 байтов данных
# s.close()
# print("Текущее время: %s" % tm.decode('ascii'))

import socket
import threading
import time

#логические флаги, об отключении и подключении клиента
shutdown = False
join = False

def receving (name, sock):
    """ Функция, для приема сообщений с сервера"""
    while not shutdown:
        try:
            while True:
                #получаем сообщения
                data, addr = sock.recvfrom(1024)
                # обязательно декодируем сообщение
                print(data.decode("utf-8"))
                # ждем 0,2 сек, на всякий
                time.sleep(0.2)
        except:
            pass

server = ("localhost", 9090)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('localhost', 0))

name = input("Name: ")

#отдельный поток для получения сообщений
rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(("["+ name +"] => join chat").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input("[You] : : ")

            if message != "":
                #обязательно кодируем сообщение
                # указываем само сообщение и куда его отправить
                s.sendto(("[" + name + "] : : " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("[" + name + "] <= left chat").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
