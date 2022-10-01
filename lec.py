# 1. Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

# import time
# now = time.time()
# print(int(str(now).split('.')[1]) % 100)

# import datetime
# now = datetime.datetime.now()
# print(int(str(now).split('.')[1]) % 100)


# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# sp = []
# for _ in range(7):
# sp.append(input())
#
# print(sp)
#
# n = int(input())
#
# flag = False
# for i in sp:
# if str(n) in i:
# flag = True
# print('Число есть в элементе списка')
# break
# if not flag:
# print('Числа в списке не оказалось')


# или 

# some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
# el = input('Введите искомое число: ')
# for i in some_list:
# if el in i:
# print('YES')
# break
# else:
# print('NO')

# 3. Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
# el = input('Введите искомую строку: ')
# first = some_list.index(el)
# second = some_list.index(el, first + 1)
# print(second)

# или

# some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
# el = input('Введите искомую строку: ')
# try:
# print(some_list.index(el, some_list.index(el) + 1))
# except:
# print(-1)