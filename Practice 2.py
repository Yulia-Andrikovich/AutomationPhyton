# Домашнее задание:
# 1. Напишите программу, которая запрашивает два числа. Выведите их среднее геометрическое, или сообщение об ошибке,
# если это сделать невозможно

from math import sqrt
print("Let's count:")
a = int(input("a: "))
b = int(input("b: "))
try:
    geometric_average = sqrt(a * b)
    print(f"Geometric average of {a} and {b} is {geometric_average}")
except ValueError:
    print(f"Can't calculate geometric average of {a} and {b}")

# 2. Напишите программу, которая будет подсчитывать общую стоимость купленных билетов, исходя из следующих условий.
# #
# a) Программа спрашивает у пользователя запрашивается количество билетов, которые он хочет купить.
#
# b) Для каждого билета пользователь должен ввести возраст посетителя.
#
# Если посетителю  меньше 18 лет, то билет будет бесплатным.
# От 18 до 25 лет — 100 руб.
# От 25 лет — полная стоимость 200 руб.
# c) При покупке больше 3 билетов пользователь получает скидку 10%
#  Программа должна вывести пользователю итоговую стоимость билетов.

number_of_tickets = int(input("Введите количество билетов:"))
full_price = 0
for ticket_index in range(number_of_tickets):
    age = int(input(f"Введите возраст для билета #{ticket_index + 1}:"))
    if age in range(18, 25):
        full_price += 100
    elif age > 25:
        full_price += 200

if number_of_tickets > 3:
    discount = full_price * 0.1
else:
    discount = 0
print(f"Total price is {full_price - discount}")