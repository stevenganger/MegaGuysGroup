# # 1 задание
# # Выведи на экран с помощью форматированных строк и функцию print() следующую информацию
# # Представься для начала (имя, фамилия). Расскажи сколько тебе лет, в каком классе учишься, какой предмет любишь больше всего
# # Код пиши прямо тут
# name = "Grisha Manosyev"
# age = 17
# clas = 11
# subject = "PE"
# print(f'Меня зовут {name}, мне {age} лет, я в {clas} классе, мой любимый предмет {subject}')
#
#
# # 2 задание
# # Тебе дан ряд переменных. Рядом с ними в комментариях укажи их тип, и изменяемость (изменяемые или неизменяемые)
# name = "Egor" #str неизменяемые
# age = 11 #int неизменяемые
# footsize = 31.5 #float неизменяемые
# favorite_games = ["GTA V", "Roblox", "Minecraft"] #list изменяемые
#
#
# # 3 задание
# # Создай переменные разных типов и положи в них значения соответствующие этому типу:
# # int, float, str, list, set
# # Обязательно подглядывай в файл с занятия!
# # Код пиши прямо тут
# int = 1
# float = 23.2
# str = "Tom"
# list = ["wew", "sheesh", "ouch"]
# set = {1,2,3,4,5}
#
#
# # 4 задание
# # Создай переменную, в которой будет храниться список из 5 любых чисел
# # Выведи на экран следующую информацию
# # Сумма всех чисел в списке
# s = [324, 100, 2, 4, 5]
# print(sum(s))


# 5 задание
# Создай переменную, в которой будет храниться список из 5 любых чисел
# Выведи на экран следующую информацию
# # Сумма всех четных чисел в списке
# t = [24, 11, 44, 200, 24]
# s = 0
# for x in t:
#     if x % 2 == 0:
#         s = s + x
# print(s)
#
#
# # 6 задание
# # Создай переменную, в которой будет храниться список из 5 любых чисел
# # Выведи на экран следующую информацию
# Сумма всех нечетных чисел в списке
# arr = [32, 3, 22, 1, 42]
# summa = 0
# for item in arr:
#     if item % 2 != 0:
#         summa = summa + item
# for i in range(0, len(arr)): # range -> [0, 1, 2, 3, 4]
#     if arr[i] % 2 != 0:
#         summa += arr[i]
# print(summa)

# 7 задание
# Создай переменную, в которой будет храниться список из 5 любых чисел
# Выведи на экран следующую информацию
# Сумма всех чисел, которые больше 3 в списке
# r = [1, 5, 4, 123, 2]
# Slog = 0
# for x in r:
#     if x > 3:
#         Slog = Slog + x
# else:
#     print()
# print(Slog)
# #
#
# # 8 задание
# # Создай переменную, в которой будет храниться список из 5 любых чисел
# # Выведи на экран следующую информацию
# # Сумма всех чисел, которые меньше 3 в списке
# e = [2, 3, 24, 1, 2]
# Slogen = 0
# for x in e:
#     if x < 3:
#         Slogen = Slogen + x
# else:
#     print()
# print(Slogen)
#
#
# # 9 задание
# # Создай переменную, в которой будет храниться список из 5 любых чисел
# # Выведи на экран следующую информацию
# # Сумма всех чисел, которые больше 3 и меньше 7 в списке
# d = [2, 6, 24, 1, 5]
# Sloge = 0
# for x in d:
#     if 7 > x > 3:
#         Sloge = Sloge + x
# else:
#     print()
# print(Sloge)
#
