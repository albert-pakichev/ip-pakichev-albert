# n1=2
# n2=n1
# n1=4
# print(f'n1={n1} n2={n2}')
# # неизменяемые объекты int float complex str tuple- immutable objects
# # изменяемые объекты set list dict - mutable objects
# sp1=[1,2,3]
# sp2=sp1
# # sp2.append(4)
# # print("sp1=",sp1,"sp2=",sp2)
# #передача аргументов по ссылке/значению
# def modify(lst):
#     lst.append('new')
#     return lst
# my_list=[1,2,3]
# mod_list=modify(list(my_list))
# # функция вернула измененный список
# print('mod_list=',mod_list)
# #Но исходный список тоже изменился, подобное явление нежелательно для функции
# print("my_list=",my_list)
# my_list=[1,-2,-4,0,5,-2]
# #Удаляем все отрицательные элементы
# for el in my_list:
#     if el<0:
#         my_list.remove(el)
# print("1)my_list after remove-->", my_list)
# #передача аргументов по ссылке/значению
# #если нужно сделать копию со всеми вложениями изменямыми обьектами, используем
# import copy
# sp=[[2,3],[4,6,[7,8]]]
# sp_copy=copy.deepcopy(sp)
# sp[0].append(10)
# print('sp_copy=',sp_copy)
# # print('sp',sp)
# matrix=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# print("matrix=",matrix)
# for i,line in enumerate(matrix):
#         for j,el in enumerate(line):
#                 print("matrix[{}][{}]={}".format(i,j,matrix[i][j]))
# # пример транспортипрования(поворота) матрицы
# print('rotate_matrix=',list(map(list,zip(*matrix))))
# people={}
# if people.get("name"):
#         name=people["name"]
# else:
#         name="Безымянный"
# print(name)
# print(people.get('name') or "Безымянный")
# print(5 or u_var)
# тернарный оператор истина if-условие, else- иначе
# d={"name":"Vasya"}
# print(d.get("name") if d.get("name") else"Безымянный")
# оператор is-является ли
# c=[1,2]
# d=c
# e=[1,2]
# c is d
# c is e
# # генераторы списков и словарей
# import random
# lst_g=[random.randint(-10,10) for _ in range(10)]
# print('lst_g=',lst_g)
# #Отбрасываем все отрицательные значкения списка
# only_positive=[el for el in lst_g if el>=0]
# # print('only_positive=',only_positive)
# keys="abxdefg"
# values=range(10)
# dict_g={key:value for key,value in zip(keys,values)}
# print('dict_g=',dict_g)
# dict2_g={el:el+1 for el in [1,4,6,8]}
# print('dict2_g=',dict2_g)
# регулярные выражения
# print('Hello \n world')
# print(r'Hello \n world')
# re.match
# import re
# string='This is a simple test message for test'
# string2='test'
# pattern1='test$'
# pattern2='^test'
# pattern3='^test$'
# print(re.search(pattern1,string)is None)
# print(re.match(pattern2,string))
# print(re.match(pattern3,string))
# print(re.match(pattern3,string2)is None)
# found=re.findall(r'test',string)
# print(found)
# import re
# pattern='[0-9]+k'
# string='if 300 spartans were so brave,so 500 spartans'\
#         'could destroy more than 10k warriors of Darius? but 15k and even 20k'
# print(re.findall(pattern,string))
# import re
# html='<p style="margin-left:10px;">text'\
# '<b class="super-bold>'
# pattern='<[^>]+>'
# print(re.findall(pattern,html))