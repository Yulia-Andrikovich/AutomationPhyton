# Задача 1
# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.

def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result

print(multiply())
print(multiply(1, 2))
print(multiply(1, 2, 3))


list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]
list3 = [1, 2, 3, 4, 5, 6, 7]
def multiplyList (myList):
    result = 1
    for i in range(0, len(myList)):
        result = result * myList[i]
    return result

print(multiplyList (list1))
print(multiplyList (list2))
print(multiplyList (list3))

# Задача 2
# Выведите длину каждого элемента в списке.
# a = ["123", "1234", "4567", "987654"]

list_numbers = ["123", "1234", "4567", "987654"]
len_numbers = list(map(lambda x: len(str(x)), list_numbers))
print(len_numbers)

# Задача 3
# Отфильтруйте из заданного списка только четные элементы.
[-2, -3, 0, 1, -1, 2, 4]

numbers = [-2, -3, 0, 1, -1, 2, 4]
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num)
print(result)

