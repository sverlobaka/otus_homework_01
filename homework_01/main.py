"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_even(in_num):
    if (in_num % 2) == 0:
        return True
    elif (in_num % 2) != 0:
        return False

def is_odd(in_num):
    if (in_num % 2) != 0:
        return True
    elif (in_num % 2) == 0:
        return False

def is_prime(in_num):
    if in_num == 0 or in_num == 1:
        return False
    count = 0
    for i in range(2, in_num // 2 + 1):
        if (in_num % i == 0):
            count = count + 1
    if count == 0:
        return True
    else:
        return False

def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == EVEN:
        result = filter(is_even, numbers)
        return list(result)
    elif filter_type == ODD:
        result = filter(is_odd, numbers)
        return list(result)
    elif filter_type == PRIME:
        result = filter(is_prime, numbers)
        return list(result)