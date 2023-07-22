# 1.Создайте список из случайных чисел. Найдите номер его последнего локального
# максимума (локальный максимум — это элемент, который больше любого из своих соседей).
# import random
#
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)
# local_max = 0
# for i in range(1, len(some_list) - 1):
#     if some_list[i] > some_list[i - 1] and some_list[i] > some_list[i + 1]:
#         local_max = some_list[i]
# print(local_max)
# print(i)

# 2.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
# import random
# count = int(input('введите кол-ва элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(1,10)
#     some_list.append(number)
# print(some_list)
# count1 = 0
# for i in range(1, len(some_list)-1):
#     if int(some_list[i]) == int(some_list[i + 1]):
#         count1 +=1
# print(count1)


# 3.Создайте списоr из случайных чисел.Найдит второй максимум.
# a = [1, 2, 3]  # Первый максимум == 3, второй == 2

# import random
# count = int(input('введите кол-ва элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(1,10)
#     some_list.append(number)
# print(some_list)
# some_list.sort()
# print(some_list[-2])

# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.
# import random
# count = int(input('введите кол-ва элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(1,10)
#     some_list.append(number)
# print(some_list)
# q = 0
# for i in range(0, len(some_list)-1):
#     if int(some_list[i]) != int(some_list[i + 1]):
#         q += 1
# print(q + 1)
