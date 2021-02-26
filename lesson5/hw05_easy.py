# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

from random import randint

a = []
b = []
for i in range(10):
    a.append(randint(0, 21))

for i in a:
    c = i ** 2
    b.append(c)
print(a, b)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


a = ["банан", "яблоко", "персик", "апельсин", "киви"]
b = ["банан", "яблоко", "апельсин", "мандарин",]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

from random import randint

a = []
b = []
for i in range(15):
    a.append(randint(0, 50))

if i % 3 == 0:
    b.append(i)

if i >= 0:
    b.append(i)

if i % 4 != 0:
    b.append(i)

print(b)




