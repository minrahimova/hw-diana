
__author__ = "Минрахимова Диана Рамилевна"

# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"
a = input("Введите ваш возраст - ")
a = int(a)
if a >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользоваться данным ресурсом можно только с 18 лет")


#Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...
nambers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
rezultat = []
a = input("Четные или нечетные? - ")
if a == "четные":
    for i in nambers:
        if i % 2 == 0:
            rezultat.append(i)
    print("четные - ", rezultat)
elif a == "нечетные":
    for i in nambers:
        if i % 2 != 0:
            rezultat.append(i)
    print("нечетные - ", rezultat)
else:
    print("Я не понимаю, что вы от меня хотите...")


# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
x = int(input("x = "))
mx = 0
while x > 0:
    с = x % 10
    if с >= mx:
        mx = с
    x //= 10
print(mx)

# some fixes