# Project Euler - Problem 21 - Amicable numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.


def foo(n):
    """Функция определяющая количетво делителей. Принимает число возвращает сумму делителей"""
    t = []  # Количество делителей которое мы будем наполнять.
    for i in range(1, n):
        if n % i == 0:
            t.append(i)
    k = sum(t)
    return k


def bar():
    """Функция генерирует число, отправляет его в функцию foo, затем сверяет на дружественные числа"""
    total = []
    n = 1

    while n < 10000:
        n += 1
        z = foo(n)
        if z != n and n == foo(z):
            total.append(n)

    return sum(total)


if __name__ == '__main__':
    print(bar())
