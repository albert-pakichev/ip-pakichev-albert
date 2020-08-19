# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# # for i in range(0,8,2):
# #     print(i)
# # print(abs(-2))
# print(max([1,2,3,4,5]
# x=round(2.56,1)
# print(x)
# x=sum([2.56,1,4])
# print(x)
# x=type('')
# # print(x)
# x=[1,2,4,5]
# for i,y in enumerate(x):
#     print(i,y)
# def summ(a,b):
#     return a+b
#     """"""
#     Документирование функции
# """""""
# x=5
# y=6
# s=summ(x,y)
# f=lambda x:x**2
# print(f(4))
# x=5
# def outside():
#     y=10
#     def inside():
#         z=15
#         print('inside x:{},y:{},z:{}'.format(x,y,z))
#     inside()
#     print('outside x:{},y:{},z:{}'.format(x,y,'z недоступна'))
# outside()
# print('inside x:{},y:{},z:{}'.format(x,'y недоступна','z недоступна'))
# x=5
# def wrapper():
#     def test1():
#         x=10
#         print('test1 x=',x)
#     def test2():
#         print('test2 x=',x)
#     def test3():
#             global x
#         print('test3 x=',x)
#         x=25
#     test1()
#     test2()
#     test3()
# wrapper()
# print('after wrapper x=',x)
# def average(*args):
#     summ=0
#     for arg in args:
#         summ+=arg
#     return summ/len(args)
# print(average(1, 2, 3))
# def print_info(**kwargs):
#     print("You name is %s %s. You age is %s. And your adress is:%s"%
#           (kwargs["name"],kwargs["surname"],kwargs["age"],kwargs["adress"]))
# print_info(name="Альберт",surname="Пакичев",age="24",adress="Подстепки")

# def welcome(name="Инкогнито"):
#     print("Приветствую вас,%s"%(name))
# welcome('Ivan')
# welcome()
# a=[1, 2, 4]
# b=[3, 4]
# c=[5, 6, 0]
# for i in zip(a,b,c):
#
# print(list(map(lambda x:x*x,[2,5,12,-2])))
# print(list(filter(lambda x:x>2,[2,10,-10,8,2,0,14])))
# # print(list(filter(len,["",'not null','bla','10'])))
# import os
# path=os.path.join('yt.odt')
# f=open(path,'r',encoding='UTF-8')
# print(f.readlines())
# f.close()
# path=os.path.join('files','text.txt')
# f=open(path,'r',enconding='UTF-8')
# wated_symbol="+"
# for line in f:
#     if wanted_symbol in line:
#         print(line)
#         # break