
__author__ = "Минрахимова Диана Рамилевна"

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print("{0:>10}".format('яблоко'))
print("{0:>10}".format('банан'))
print("{0:>10}".format('киви'))
print("{0:>10}".format('арбуз'))



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
a = [1, 2, 3, 4, 5, 52, 65]
b = [1, 2, 3, 4, 5, 122, 94]
for i in a:
    if i in b:
        a.remove(i)
print(a)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
a = [1, 2, 5, 122, 94, 58, 24, 63]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i/4)
    else:
        b.append(i*2)
print(b)

