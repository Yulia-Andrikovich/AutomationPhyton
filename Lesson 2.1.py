# float
a = 0.28
b = 1.5

print(type(a))
print(type(b))

# str Строки
name = "Kate"
city = 'Minsk'

name = "I'm Kate"
about = 'Я люблю "Python"'

# Работа с индексами
a = "Kate"
print(a[0])
print(a[1:3])
print(a[2:])
print(a[:3])
print(a[::2])
print(a[::-1])
print(a[-1])
print(a[-3:-1])

# функция len() позволяет узнать длину строки
print(len(a))

# привести все буквы к верхнему регистру
print(a.upper())

# привести все буквы к нижнему регистру
print(a.lower())

# Функций и методов строк гораздо больше. С полным списком можно ознакомиться самостоятельно по ссылке:
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

# Преобразование строк
int_num = int(input("Введите целое число: "))  # вводим, например, 2869
print(int_num)
# 2869
print(type(int_num))  # тип данных в переменной - int
# <class 'int'>


# Boolean
print(1 > 10)
print(1 < 10)
print('k' in 'kate')

# Tuple
date = (6, 'oktober', 2022)
print(date[0])
print(date[1])
print(date[2])

# Приведение типов
print(float(1))
print(int(1.2))
print(int(1.9))

# Изменяемые типы данных
# Cписок
s = []
s = [1, 'kate', (1, 'a')]

pets = ['cat', 'dog', 'finch', 'cow']
pets.append('wolf')
print(pets)
print(len(pets))

# Метод Index
# Возвращает положение первого индекса
l = [4, 1 ,5 ,4 ,10]
print(l.index(4))
# Метод Count
# Считает количество раз, когда значение появлется в списке
l = [1, 4, 5, 4, 7, 4]
print(l.count(4))
# Метод Sort
l = [1, 4, 5, 4, 7, 4]
print(l.count(4))
l.sort(reverse = True)
print(l)
[7, 5, 4, 4, 4, 1]
# Метод Remove
l.remove(4)
print(l)
[7, 5, 4, 4, 1]
# Метод Pop
print(l.pop(1))
5
print(l)
[7, 4, 4, 1]
# Метод Extend
l = [7,3,3]
l.extend([4,5])
print(l)
[7, 3, 3, 4, 5]
print([1,2] + [3,4])
[1, 2, 3, 4]
# Метод Insert
l.insert(4, [1,2,3])
print(l)
[7, 3, 3, 4, [1, 2, 3], 5]

# Словари
dict_1 = {}
dict_1 = {1: 'dog', 2: 'cat'}
dict_2 = {'pet': "dog", 1: [2, 7, 9]}

dict_3 = dict({11: 'dogg', 22: 'catt'})

dict_4 = {1: {'student1': 'Ivan', 'student2': 'Olga'}, 2: {'student1': 'Ivan', 'student2': 'Olga'}}

dict_5 = {
    "Group": "Automatization",
    "language": "Python",
    "number": 1
}

# множества (set)
st = {'a', 'b', 'c', 'd'}  # используя синтаксис { }
A = [1, 1, 2, 3, 2]
B = set(A)
print(B)

# ПРАКТИКА 1
# Вам дан словарь banks с указанием процентных ставок по вкладам в разных банках. В словаре ключ — название банка,
# значение — процент. Ваша задача написать программу, в результате которой будет сформирован список sum значений —
# накопленные средства за год вклада в каждом из банков. На вход программы с клавиатуры пользователь вводит сумму
# money, которую  человек планирует положить под проценты.
# banks = {'SBER': 3.2, 'VTB': 2.4, 'ALFA': 4.92, 'PRIOR': 3.0}
# Пример работы программы:
# money = 100000
# sum = [3200, 2400, 4920, 3000]
banks = {'SBER': 3.2, 'VTB': 2.4, 'ALFA': 4.92, 'PRIOR': 3.0}
money = int(input("Введите сумму вклада: "))
sum = list([
    round(money / 100 * banks['SBER']),
    round(money / 100 * banks['VTB']),
    round(money / 100 * banks['ALFA']),
    round(money / 100 * banks['PRIOR'])
])
print("sum = ", sum)

banks = {'SBER': 3.2, 'VTB': 2.4, 'ALFA': 4.92, 'PRIOR': 3.0}
money = int(input("Введите сумму вклада:"))
sum = []
for key in banks:
    sum.append(float(money * banks[key] / 100))
print("sum=", sum)

# Домашнее задание:
# 1. Напишите программу, запрашивает у пользователя его год и месяц рождения в числах, и выводит, сколько ему лет
year = int(input("Год: "))
month = int(input("Месяц: "))

if month < 10:
    print("Вам", 2022 - year, "лет")
else:
    print("Вам", 2021 - year, "лет")

date = float(input("Введите дату рождения в формате год.месяц: "))
print("Вам", int(2022.10 - date), "лет")

# 2. Напишите программу, которая запрашивает у пользователя число минут и выводит их в виде дни: часы:минуты
mins = int(input("Минуты: "))

days = mins // 1440
mins -= days * 1440
hours = mins // 60
mins -= hours * 60

print(f"{days}:{hours}:{mins}")
# 3. Напишите программу, которая запрашивает у пользователя строку и выводит, является ли она палиндромом.Строка
# не будет содержать пробелов или специальных символов.
s = str(input("Строка: "))
s_rev = "".join(reversed(s))
if s == s_rev:
    print("Палиндром")
else:
    print("Не палиндром")