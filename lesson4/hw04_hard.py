
__author__ = "Минрахимова Диана Рамилевна"

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# запрашиваем у пользователя дроби по отдельности, в смешанном виде и записываем их в переменные, знак тоже

a = input("Введите первый элемент примера: такого вида: n x/y - ")
b = input("Введите знак - ")
c = input("Введите второй элемент примера: такого вида: n x/y - ")

# сначало отделяем целую часть от десяичной

tsela_chast_1, drobna1 = a.split(" ")
tsela_chast_2, drobna2 = c.split(" ")

# теперь десятичную  разделяем на числитель и знаменатель

chislitel1, znamenatel1 = drobna1.split("/")
chislitel2, znamenatel2 = tsela_chast_1.split("/")

# дальше переводим все в int

chislitel1 = int(chislitel1)
chislitel2 = int(chislitel2)
znamenatel1 = int(znamenatel1)
znamenatel2 = int(znamenatel2)
tsela_chast_1 = int(tsela_chast_1)
drobna2 = int(drobna2)

# переводим числители дробей в неправильную, умнажая целую часть на знаменатиль и прибавляя числитель

d = znamenatel1 * chislitel1 + chislitel1
e = znamenatel2 * chislitel2 + chislitel2

# создаем функцию по каторой ищим общий знаменатьль

def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)
k = nok(chislitel1, chislitel2)

# ищим дополнительные множители, деля наибольший знаменятель на неправильную дробь

f = k // d
g = k // e

# сама функция

def res(c, d, e, f, g, ):
    if c == "+":
        i = (d * e) + (f * g)
        return i
    elif c == "-":
        j = (d * e) - (f * g)
        return j
l = res(b, d, f, e, g)

# переводим обратно в смешанную дробь

h = l
n = h // k
p = n % k
print(n, p, "/", k)


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os
path = os.path.join("data", "workers")
path_1 = os.path.join("data", "hours_of")
with open(path, "r", encoding="UTF-8") as w:
    lines = w.readlines()
    hours_workers = []
    for line in lines[1:]:
        line_worker = line.split()
        hours_workers.append(line_worker)
with open(path_1, "r", encoding="UTF-8") as w:
    lines = w.readlines()
    list_workers = []
    for line in lines[1:]:
        line_worker = line.split()
        list_workers.append(line_worker)
def lol(a, b):
    c = a // b
    return c
def lol1(e, f):
    g = e * f
    return g
for i in list_workers:
    for j in hours_workers:
        if i[0] in j and i[1] in j:
            print("Имя и фамилияя совпали, можно считать")
            d = lol(int(j[2]), int(j[4]))
            h = lol1(d, int(i[3]))
            k = int(j[4]) - int(i[3])
            n = int(i[2]) - int(j[4])
            if k > 0:
                l = int(j[2]) - (k * h)
                print("Вы отработали меньше, Ваша зарплата - ", l)
            elif k < 0:
                m = int(j[2]) + (h * 2 * n)
                print("Вы отработалимбольше, Ваша зарплата - ", m)
            else:
                p = int(j[2])
                print("Ваша зарплата - ", p)