# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect("shop.db")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT id FROM kategories
            WHERE kategory = 'спорт'""").fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem)