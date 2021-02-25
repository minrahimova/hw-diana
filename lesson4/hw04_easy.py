
__author__ = "Минрахимова Диана Рамилевна"

# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили


def convert(km):
    a = km * 1.609
    return a


miles = convert(int(input("Напишите растояние в км - ")))


print("Ваше растояние в милях - ", miles)


# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    step = pow(10, ndigits)
    return int(number * step + 0.5)/step


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)


def lucky_ticket(ticket_number):
    str_ticket = str(ticket_number)
    first_part_ticket = str_ticket[:3]
    second_part_ticket = str_ticket[3:]

    result_first = 0
    result_second = 0


    for i in first_part_ticket:
        result_first += int(i)
    for i in second_part_ticket:
        result_second += int(i)
    if result_first == result_second:
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))