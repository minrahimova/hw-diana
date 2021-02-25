
__author__ = "Минрахимова Диана Рамилевна"

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fib1 = 1
    fib2 = 1
    fibonacci_list = []
    fibonacci_list.append(fib1)
    fibonacci_list.append(fib2)
    for i in range(0, m + 1):
        next_fib = fib1 + fib2
        fib1 = fib2
        fib2 = next_fib
        fibonacci_list.append(next_fib)
    return fibonacci_list[n:]


start = int(input("Введите начало ряда - "))
end = int(input("Введите конец ряда - "))
fibonacci_list = fibonacci(start, end)
print(fibonacci_list)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


sort_to_max = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]


def diana_bubble_sort(sort_to_max):
    sort_to_max = sort_to_max.copy()
    new_list = []
    while sort_to_max:
        minimum = sort_to_max[0]
        for x in sort_to_max:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        sort_to_max.remove(minimum)
    return new_list


def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)


    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(diana_bubble_sort(sort_to_max))
print(bubble_sort(sort_to_max))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filter_list(fucnt, param_b):
    end_list = list()
    for x in param_b:
        if fucnt(x) == True:
            end_list.append(x)
        else:
            continue
    return end_list


print((filter_list((lambda x: x > 5), param_b=[1, 100, 500, 7, 8, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


A1 = (1, 1)
A2 = (2, 4)
A3 = (6, 4)
A4 = (7, 1)


def is_parallelogram(a, b, c, d):
    if a[0] + c[0] == b[0] + d[0] or a[1] + c[1] == b[1] + d[1]:
        return True
    else:
        return False


if is_parallelogram(A1, A2, A3, A4):
    print("это параллелограмм")
else:
    print("это не параллелограмм")