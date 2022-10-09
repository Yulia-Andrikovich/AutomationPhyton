banks = {'SBER': 3.2, 'VTB': 2.4, 'ALFA': 4.92, 'PRIOR': 3.0}
money = int(input("Введите сумму:"))
sum = [int(money * banks ['SBER'] / 100), int(money * banks['VTB'] / 100), int(money * banks ['ALFA'] / 100), int(money * banks ['PRIOR'] /100)]
print(sum)

m = int(input("Введите минуты"))
d = m // 1440
m -= d * 1440
h = m//60
m -= h * 60
print(f"{days}:{hours}:{mins}")


inValue = int(input("Enter minuts\n"))
days = inValue // (60 * 24)
hours = (inValue - days * 24 * 60) // 60
mins = inValue - (days * 24 * 60 + hours * 60)
print ("%02d:%02d:%02d" % (days, hours, mins))


import datetime
min = int(input("Введите минуты"))
time = datetime.timedelta(minutes =min)
print(time)

year = int(input("Введите год рождения"))
month = int(input("Введите месяц рождения"))
day = int(input("Введите число рождения"))
from datetime import date
birth_date = date(year, month, day)
days_in_year = 365.2425
age = int((date.today() - birth_date).days / days_in_year)
print(age)



    slovo = str(input())
    a = slovo[::-1]
    if slovo == a:
        print("Palindrome")
    else:
        print("Not Palindrome")