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

