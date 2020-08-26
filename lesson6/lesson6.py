# #обработка исключений
# f=open('1.txt')
# ints=[]
# try:
#     for line in f:
#         ints.append(int(line))
# except ValueError:
#     print('Это не число. Выходим')
# except Exception:
#     print('это что еще такое?')
# else:
#     print('Все хорошо')
# finaly:
#     f.close()
#     print('Я закрыл файл')
# print("start")
# try:
#     val=int(input("input number:"))
#     tmp=10/val
#     print(tmp)
# except (ValueError,ZeroDivisionError):
#     print("Error!")
# print("stop")
#генерация исключений принудительно
# try:
#     raise Exception("Some exception")
# except Exception as e:
#     print("Exception exception"+str(e))
# import math
# print(math.sqrt(4))
# #другой вариант подключения модуля
# from math import sqrt
# print(sqrt(4))
# #импортируем сразу несколько функций
# from math import sqrt,sin,cos
# print(sin(0.2))
# #Создание собственных модулей
# def do_something():
#     return "i`m func do_something in module lib1"
# def more_then_one(num):
#     return num>1
# import lib as my_lib
# print(mt_lib.do_something())
# print(my_lib.more_then_one(6))
                                        # Модуль ОС
# import os
# print('os.name=',os.name)
# print('os.getcwd()=',os.getcwd())
# dir_path=os.path.join(os.getcwd(),'NewDir')
# try:
#     os.mkdir(dir_path)
# except FileExistsError:
#     print('Такая директория уже существует')
                            #Модуль SYS
# import sys
# #Список аргументов запуска скрипта
# #Первым аргументом является полный путь к файлу скрипта
# print('sys.argv=',sys.argv)
# #Список путей для поиска модулей
# print('sys.path=',sys.path)
# #Полный путь к интерпритатору
# print('sys.executable=',sys.executable)
# #Словарь имен загруженных модулей
# print('sys.platform=',sys.platform)
# while True:
#     key=input("press 'q' to Exit")
#     if key=='q':
#         sys.exit()
#         #Вызов данной функции мгновенно завершает работу модуля
#все сделать проще argparse
# import sys
# import argparse
# def createParser():
#     parser=argparse.ArgumentParser()
#     parser.add_argument('name',nargs='?',default='мир')
#     return parser
# if __name__ =='__main__':
#     parser=createParser()
#     namespace=parser.parse_args(sys.argv[1:])
#     print("Привет,{}!".format(namespace.name))
                #установка пакетов с помощью pip
