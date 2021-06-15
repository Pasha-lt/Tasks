# Project Euler - Problem 025 - 1000-digit Fibonacci number
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def foo():
    a = [1, 1]  # ряд фибоначи
    n = 0  # переменная для перебора индекса.
    while True:
        if len(str(a[-1])) >= 1000:
            return len(a)  # Нам нужно вернуть порядковый номер числа с 1000 цифрами это и будет длина ряда.
        else:
            a.append(a[n]+a[n+1])  # Суммируем два предвидущих числа чтобы узнать третье.
            n += 1


print(foo())
