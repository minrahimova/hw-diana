
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

a = input("Введите первый элемент примера: такого вида: n x/y - ")
znak = input("Введите знак - ")
c = input("Введите второй элемент примера: такого вида: n x/y - ")

# сначало отделяем целую часть от десяичной

tsela_chast_1, drobna1 = a.split(" ")
tsela_chast_2, drobna2 = c.split(" ")

# теперь десятичную  разделяем на числитель и знаменатель

chislitel1, znamenatel1 = drobna1.split("/")
chislitel2, znamenatel2 = drobna2.split("/")

# дальше переводим все в int

chislitel1 = int(chislitel1)
chislitel2 = int(chislitel2)
znamenatel1 = int(znamenatel1)
znamenatel2 = int(znamenatel2)
tsela_chast_1 = int(tsela_chast_1)
tsela_chast_2 = int(tsela_chast_2)


# создаем функцию по каторой ищим общий знаменатьль
def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


obsh_znam = nok(znamenatel1, znamenatel2)


# переводим числители дробей в неправильную, умнажая целую часть на знаменатиль и прибавляя числитель
smesh_ch1 = obsh_znam * tsela_chast_1 + chislitel1 * obsh_znam / znamenatel1
smesh_ch2 = obsh_znam * tsela_chast_2 + chislitel2 * obsh_znam / znamenatel2


# сама функция
def res(znak, smesh_ch1, smesh_ch2, obsh_znam):
    celoe = 0
    chast = 0

    if znak == "+":
        summa = smesh_ch1 + smesh_ch2
        celoe = summa // obsh_znam
        chast = summa % obsh_znam
    elif znak == "-":
        raznost = smesh_ch1 - smesh_ch2
        celoe = raznost // obsh_znam
        chast = raznost % obsh_znam

    return "{} {} / {}".format(int(celoe), int(chast), obsh_znam)


l = res(znak, smesh_ch1, smesh_ch2, obsh_znam)


print(l)


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

with open(path_1, "r", encoding="UTF-8") as w:
    lines = w.readlines()
    hours_workers = []
    for line in lines[1:]:
        line_worker = line.split()
        hours_workers.append(line_worker)

with open(path, "r", encoding="UTF-8") as w:
    lines = w.readlines()
    list_workers = []
    for line in lines[1:]:
        line_worker = line.split()
        list_workers.append(line_worker)


def stoimost_chasa(norm_zp, norm_chasi):
    za_chas = norm_zp // norm_chasi
    return za_chas


def cena_za_vse_vremya(stoimost, chasi):
    total = stoimost * chasi
    return total


for i in list_workers:
    for j in hours_workers:
        if i[0] in j and i[1] in j:
            print("Имя и фамилияя совпали, можно считать")
            norm_zp = int(i[2])
            norm_chasi = int(i[4])
            otrabotal = int(j[2])
            za_chas = stoimost_chasa(norm_zp, norm_chasi)
            zarplata = cena_za_vse_vremya(za_chas, otrabotal)
            pererabotka = otrabotal - norm_chasi

            if pererabotka < 0:
                print("Вы отработали больше, Ваша зарплата - ", zarplata)
            elif pererabotka > 0:
                zarplata += za_chas * 2 * pererabotka
                print("Вы отработали больше, Ваша зарплата - ", zarplata)
            else:
                p = int(j[2])
                print("Ваша зарплата - ", zarplata)