# Урок 2. Циклы (for, while)

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input('Введите количество монет '))
# orel = 0 
# reshka = 0
# for i in range(n):
#     x = int(input('Орел(1) или Решка(0)? '))
#     if x == 1:
#         orel += 1
#     else:
#         reshka += 1
# if orel < reshka:
#     print(f'Меньше всего монет с орлом, переверните {orel} монет с орла на решку.')
# elif orel == reshka:
#     print(f'Количество орлов и решек одинаково, по {orel} штук')
# else:
#     print((f'Меньше всего манет с решкой, переверните {reshka} монет с решки на орла.'))



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# s = a + b
# p = a * b
# b1 = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)
# a1 = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)
# print(f'Загаданные числа {a1} и {b1}')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

# n = int(input('Введите число N: '))
# i=0
# while 2 ** i <= n:
#      print(2 ** i)
#      i += 1

