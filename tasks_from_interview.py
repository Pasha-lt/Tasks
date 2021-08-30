# Нужно отсеить в списке числа меньшие и раные 5
a = [3, 3, 3, 4, 5, 7, 7, 8, 9, 0, 5, 5, 5, 7, 8, 9, 132]
b = filter(lambda x: x>5, a)
print(list(b))

# Нужно поменять местами ключи и значения в словаре
c = {123:'123', (12,23,4):12, 'kie':'ffds'}
d = {x:y for y,x in c.items()}
print(d)

# другая компания
# Напишите программу которая будет считать факториал, используйте функциональное программирование. 
from functools import reduce

number = int(input("Введите число с которого мы будем брать факториал: "))
numbers_list = range(1, number+1)
factorial = reduce(lambda x,y:x*y, numbers_list)
print(factorial)


# другая компания
# tsak 1
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
