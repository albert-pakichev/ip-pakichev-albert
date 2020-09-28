# #импортируем библиотеку, соотв. типу нашей базы данных
# import sqlite3
# #создаем соединение с нашей базой данных
# conn =sqlite3.connect('chinook_sqlite.sqlite')
# #создаем курсор- это специальный объект, кототрый делает запросы и получает их результаты
# cursor=conn.cursor()
# #тут будет код для работы с базой данных
# #код дальнейших примеров вставлять в это место
# #код
# # cursor.execute("SELECT Name FROM artists ORDER BY Name LIMIT 3")
# #
# # #получаем результат сделанного запроса
# # results=cursor.fetchall()
# # results2=cursor.fetchall()
# #делаем insert запрос к базе данных, используя обычный sql-синтаксис
# cursor.execute("Insert into artists values (Null,'A Aargh!')")
#
# #если мы не рпсто читаем, но и вносим изменения в базу данных-необходимо сохранить транзакцию
# conn.commit()
#
# #проверяем результат
# new_artists = [
#     ('A Aagrh!',),
#     ('A Aagrh!-2',),
#     ('A Aagrh!-3',),
# ]
#
# for row in cursor.execute('SELECT Name from artists ORDER BY Name LIMIT 3'):
#        print(row)
# #
# # cursor.executemany("insert into artists values (Null,?);", new_artists)
# # cursor.execute("SELECT Name from artists ORDER BY Name LIMIT:limit",{"limit":3})
# # # cursor.execute("SELECT Name FROM artists ORDER BY Name LIMIT 3")
# # results = cursor.fetchall()
# # print(results)
# # print(results2)
#
#
#
# # не забываем закрыть соединение
# conn.close()
# #обработка ошибок
# try:
#     cursor.execute(sql_statement)
#     result = cursor.fetchall()
# except sqlite3.DatabaseError as err:
#     print("Error:",err)
# else:
#     conn.commit()
# finally:
#     conn.close()

