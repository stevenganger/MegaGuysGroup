# Задание 1
# 48339
# alphabet = '0123456789A'
# for x in alphabet:
#     a = '982' + x + '8'
#     b = '194' + x + '7'
#     if (int(a, 11) + int(b, 11)) % 58 == 0:
#         print((int(a, 11) + int(b, 11)) // 58)
# Ответ: 2931
# Задание 2
# 48382
# alphabet = '0123456789ABCDEF'
# for x in alphabet:
#     a = int('8' + x + '84' + x , 16)
#     b = int('78' + x + '34' , 16)
#     if (a + b) % 23 == 0:
#         print((a + b) // 23)
#         break
# Ответ: 45963
# Задание 3
# 7761
# m = 4**2020 + 2**2017 - 15
# r = bin(m)[2:]
# print(r.count('1'))
# Ответ:2015
# Задание 4
# 17334
# def calc (x, a, b):
#     s = ''
#     x = int(str(x), a)
#     while x > 0:
#         s += str(x % b)
#         x //= b
#     return s[::-1]
# r = 2*216**6 + 3*36**9 - 432
# result = calc(r, 10, 6)
# print(result.count('5'))
# Ответ: 14
# Задание 1
# Напишите функцию, которая принимает на вход два числа и возвращает:
# сумму, произведение, разность, частное, максимальное, минимальное из них
# def universal (a, b):
#     summ = a + b
#     pr = a * b
#     razn = a - b
#     chasta = a / b
#     chastb = b / a
#     minim = min(a,b)
#     maxim = max(a,b)
#     return(print(summ,pr,razn,chasta,chastb,minim,maxim))
# Задание 2
# Напишите лямбда-функцию, которая принимает на вход число и проверяет его четность
# f = lambda x: x % 2 == 0
# print(f(4))
# Задание 3
# Попробуйте по памяти написать функцию calc(x, a, b)
# Сделайте форматный вывод по типу: "x = 123, a = 10, b = 7, result = 123"
# def calc (x, a, b):
#     s = ''
#     x += int(str(x), a)
#     while x > 0:
#         s += str(x % b)
#         x //= b
#     return s[::-1]
# Задание 4
# Напишите функцию, которая принимает на вход число и возвращает его факториал
# Без использования math.factorial!
# def factorial (x):
#     if x < 2:
#         return 1
#     else:
#         return x * factorial(x-1)
# g = factorial(3)
# print(g)
# Блок Extra задач
# Задание 1
# Вам дана фотография ноутбука. Ответьте на следуюший вопрос:
# С каким моментом затянут каждый из самых туго затянутых винтов в этом компьютере? Ответ следует выразить в ньютон-метрах.
# https://dropmefiles.com/kYUbB
# Ответ: пока не известно
# Задание 2
# Вам дана фотография улицы. Ответьте на следуюший вопрос:
# Какие два слова висели 26 лет назад на месте этих следов от логотипа Открытия?
# https://dropmefiles.com/yZcGI
# Ответ: Институт красоты