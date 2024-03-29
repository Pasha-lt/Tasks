# потрібно відсіяти в списку меньше і рівні 5
a = [3, 3, 3, 4, 5, 7, 7, 8, 9, 0, 5, 5, 5, 7, 8, 9, 132]
b = filter(lambda x: x>5, a)
print(list(b))

# Потрібно поміняти ключі і значення місцями в словнику.
c = {123:'123', (12,23,4):12, 'kie':'ffds'}
d = {x:y for y,x in c.items()}
print(d)

# інша компанія
# Напишіть програму котра буде вираховувати факторіал використовуючи функціональне програмування.
from functools import reduce

number = int(input("Введіть число з якого потрібно взяти факторіал: "))
numbers_list = range(1, number+1)
factorial = reduce(lambda x,y:x*y, numbers_list)
print(factorial)


# інша компанія
# task 1
# Нужно написать функцию которя принимает два списка и выдает список с поочередными элементами из списка 1 и 2
# [1, 2, 3, 4], [7,6,9] =>> [1, 7, 2, 6, 3, 9, 4]
def foo(list_a, list_b):
    index_number = max(len(list_a), len(list_b))
    new_list = []
    for i in range(index_number):
        try:
            new_list.append(list_a[i])
        except:
            pass
        try:
            new_list.append(list_b[i])
        except:
            pass

    return new_list

list_a = [1, 2]
list_b = [7, 6, 9]

print(foo(list_a, list_b))

# task2
# Нужно исправить код и дописать вызовы в assert'ах чтобы отработали assert'ы
class Folder(object):
    def __init__(self, name):
        self.name = name

    @property
    def path(self):
        return '/%s' % self.name


folder1 = Folder('picture')
assert(folder1.name == 'picture')
assert(folder1.path == '/picture')

assert(folder2.name == 'nature')
assert(folder2.path == '/pictures/nature')

assert(folder1.name == 'pic')
assert(folder2.path == '/pic/nature')

# Решение
class Folder(object):
    def __init__(self, name, parent_folder=None):
        self.name = name
        self.parent_folder = parent_folder

    @property
    def path(self):
        if self.parent_folder != None:
            # смотреть как на обьект, а не на строку и через path вызывать путь
            result = f'{self.parent_folder.path}/{self.name}'
        else:
            result = f'/{self.name}'
        return result


folder1 = Folder('pictures')
assert (folder1.name == 'pictures')
assert (folder1.path == '/pictures')
print('assert1')

folder2 = Folder('nature', folder1)
assert (folder2.name == 'nature')
assert (folder2.path == '/pictures/nature')
print('assert2')

# folder1.name = 'pic'
# assert(folder1.name == 'pic')
# assert(folder2.path == '/pic/nature')
# print('assert3')

print('-'*20)
folder3 = Folder('nat', folder2)
print(folder3.path)
folder1.name = 'pic'
print(folder3.path)
assert(folder1.name == 'pic')
assert(folder2.path == '/pic/nature')
print('assert3')


# Другая компания
# task_1
# Using this list of hetels:
# hotels = [{'name': 'Hilton', "locations": 2345}, {'name': "Accor", 'locations': 789}, {'name': 'W', "locations":678}]
# Please write code to create a new list of hotel names by each of these methods:
# - using for loops 
# - using list comprehensions
# - using the map() functions 

hotels = [{'name': 'Hilton', "locations": 2345}, {'name': "Accor", 'locations': 789}, {'name': 'W', "locations":678}]

# first solution, use loops
list_loop = []
for i in hotels:
    list_loop.append(i['name'])

# second solution, use list comprehensions
list_comprehension = [i['name'] for i in hotels]

# third solution, use the map
list_map = list(map(lambda hotels: hotels['name'], hotels))


print(list_map)
print(list_comprehension)
print(list_loop)

# task_2
# Write a function named word_count that takes in a string. Return a dictionary with each word in the string as the key
# end the number of times it appers as the value.



def word_count(string_a):
    string_a =string_a.replace(',', '').replace('.','')
    dict_count = {}
    for word in string_a.split():
        if word in dict_count:
            dict_count[word] +=1
        else:
            dict_count[word] = 1
    return dict_count

print(word_count('раз раз. два три'))

# task_4
# Given the list bellow, write code to remove duplicates and preserve initial order of elements occurrence.
# amenities = ['free wifi', 'breakfast', 'gym', 'breakfast', 'pool', 'restaurant']
amenities = ['free wifi', 'breakfast', 'gym', 'breakfast', 'pool', 'restaurant']

new_amenities = []
for word in amenities:
    if word not in new_amenities:
        new_amenities.append(word)

print(new_amenities)

# task_5
# Write a decorator that will print the execution of the method it decorates.

from datetime import datetime

def timeit(func):
    def wrapper(*args,  **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        all_time = datetime.now() - start
        print(all_time)
        return result
    return wrapper()

@timeit
def foo():
    pass


# task_6
# Write a function that will remember parameters passed to it and if such parameters have already been passed - will not
# waste time on their calculation in a second time. Do not use ready-made solutions, but make yours.
# As an example, you can take the following function:
# from time import sleep
# def delayed_greeting(name):
#     sleep(5)
#     return f'Hey, {name}!'
# delayed_greeting('Bob')
# delayed_greeting('Bob')

#solution_1
from time import sleep
list_optimization = []

def delayed_greeting(name):
    global list_optimization
    # list_optimization = []
    print(list_optimization)
    if name not in list_optimization:
        list_optimization.append(name)
        print('-->',list_optimization)
        sleep(5)
        return f'Hey, {name}!'

print(delayed_greeting('Bob'))
print(delayed_greeting('Bob'))


exit()
#solution2
from time import sleep

class Foo:
    list_optimization = []
    def __init__(self, name):
        self.name = name

    def delayed_greeting(self):
        if self.name not in self.list_optimization:
            self.list_optimization.append(self.name)
            sleep(5)
            return f'Hey, {self.name}!'

t = Foo('Bob')
t.delayed_greeting()
p = Foo('Bob')
p.delayed_greeting()

# Task 7
# Write a function that takes a list of numbers, and for each list element it should find the product of rest list
# elements excluding the current one.
# For example, given: [2, 5, 3, 4]
# Your function should return: [60, 24, 40, 30]
# By calculating: [5*3*4, 2*3*4, 2*5*4, 2*5*3]
from functools import reduce

def foo(list_a):
    mult_number = reduce(lambda x,y:x*y, list_a)
    # верхняя строчка вместо нижних
    # mult_number = 1
    # for i in list_a:
    #     mult_number *= i
    new_list = [int(mult_number/list_a[j]) for j in range(len(list_a))]
    return new_list

list_a = [2,5,3,4]
# print(list_a)
print(foo(list_a)) # [60, 24, 40, 30]

# Другая компания
# пример оптимизации кода когда запускаем последовательность
def foo(a):
    return a ** 2


def bar(a):
    return a - 1


print([bar(foo(a)) for a in range(4)])


# Используя команду ifconfig найти ipv4, ipv6, mtu
import os
import re

ipconfig_value = os.popen("ifconfig").read()

mtu = (re.findall(r'mtu \d\d\d\d', ipconfig_value, flags=re.MULTILINE))[0]
print(mtu)
ipv4 = (re.findall(r'inet \d*.\d*.\d*.\d*', ipconfig_value, flags=re.MULTILINE))[-1]
print(ipv4)
ipv6 = (re.findall(r'inet6 \w\w\w\w::\w\w\w\w:\w\w\w\w:\w\w\w\w:\w\w\w\w', ipconfig_value, flags=re.MULTILINE))[0]
print(ipv6)


# new interview 
'''
write function for this param.
example_true = "ab(a(b(c)d)eeezv)"
example_false1 = ")("
example_false2 = "((a)"
example_false3 = "abc())("
'''
def foo(user_string):
    value = False
    list_open_p = []
    list_close_p = []
    for index_s, symbol in enumerate(user_string):
        if symbol == '(':
            list_open_p.append(index_s)
        elif symbol == ')':
            list_close_p.append(index_s)
    if len(list_open_p) == len(list_close_p):
        for index_x in range(len(list_close_p)):
            if (list_close_p[index_x] - list_open_p[index_x]) < 0:
                return False
            else:
                value = True
        return value
    return False


example_true = "ab(a(b(c)d)eeezv)"
example_false1 = ")("
example_false2 = "((a)"
example_false3 = "abc())("
print(foo(example_true))
print(foo(example_false1))
print(foo(example_false2))
print(foo(example_false3))

# new_company 
# Написать код который будет выозвращать два ближних числа к заданому одно меньше, второе больше по значению. 
'''
8. You have a list of numbers (Integers) and target number (Integer). Task is to find in a list closest number(s) to defined target number.
Custom example:
some_list = [4, 2, 10, 7]
target = 5
Result will be: result_list = [4, 7]
'''
# solution 1
some_list = [4, 2, 10, 7]
target = 5
some_list.append(target)
some_list.sort()
target_index = some_list.index(target)
print(some_list[target_index-1], some_list[target_index+1])

# solution 2
min_value = min(some_list)
max_value = max(some_list)
for i in some_list:
    if (target-i) > 0 and i > min_value:
        print(min_value)
        min_value = i
    elif (i-target) > 0 and i < max_value:
        max_value = i
print(min_value, max_value)

# Отсортировать список через лист компрехеншн чтобы он вернул значения выше 2
old_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
new_list = [x for x in old_list if x < 3] 
print(new_list) 

# Вводиться строка слов. Программа должна вывести на экран слова строки по возрастанию их длины.
s = input('Введите предложение')
s = s.split()
s.sort(key=len)
s = ' '.join(s)
print(s)

# Написать код который в l3 добавит все елементы из l1 и l2 которые есть в двух списках
l1 = ['a', 'd', '23', 'fff', '67']
l2 = ['fgd', 'ty', '23', '67', 'fhj', 'rrew']
l3 = set(l1).intersection(set(l2))
print(l3)

#1.
a = 'qwerty'
b = 'ytrewq' # - how to get it?
print(a[::-1])

#2.
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
a == b
a is b
print(a == b) # True
print(a is b) # False

# 3.
a = [1, 2, 3]
b = a
b[0] = 100
print(a) # [100, 2, 3]
print(b) # [100, 2, 3]

"""
1. склеить два массива: [1, 2, 3, 4], [7, 8] -> [1, 7, 2, 8, 3, 4]. Длина массивов может быть разной
Использовать рекурсию
"""

def foo(list_a, list_b, new_list):
    if len(list_a) == 0:
        new_list.extend(list_b)
        return new_list
    elif len(list_b) == 0:
        new_list.extend(list_a)
        return new_list
    else:
        new_list.append(list_a[0])
        new_list.append(list_b[0])
        return foo(list_a[1:], list_b[1:], new_list)



list_a = [1, 2, 3, 4]
list_b = [7, 8]
new_list = []
print(foo(list_a, list_b, new_list))


# У вас есть массив чисел. Напишите три функции, которые вычисляют сумму этих чисел: с for-циклом, с while-циклом, с рекурсией.
def sum_for_loop(a):
    s = 0
    for x in a:
        s += x
    return s

def sum_while_loop(a):
    s = 0
    n = len(a)
    while n:
        n -= 1
        s += a[n]
    return s

def sum_recursive(a):
    if len(a) == 0:
        return 0
    return a[0] + sum_recursive(a[1:])

t = [5, 3, 4, 1, 7]
sum_for_loop(t)
sum_while_loop(t)
sum_recursive(t)

######new company########
"""
Given a string of parentheses - `()[]{}`, implement a function called `is_balanced`
that returns `True` or `False` if the parentheses are balanced
(think about a code fragment where all other characters were filtered).
We can assume only the above 6 characters exist in the input string.
"""
import pytest

def foo(text):
    dict_a = {")": "(", "}": "{", "]": "["}
    a_list = []
    for number, i in enumerate(text):
        if i in "({[":
            a_list.append(i)
        elif len(a_list) > 0:
            print(f'{a_list=}')
            if dict_a[i] == a_list[-1]:
                a_list.pop()
            else:
                return False
        else:
            return False
    return not bool(a_list)


@pytest.mark.parametrize("value_t", [
    pytest.param("{}[]"),
    pytest.param("{()}")])
def test_foo_positive(value_t):
    assert foo(value_t) == True


def test_foo_negative():
    assert foo("([)]") == False
    assert foo("}{") == False
    
######new company########
