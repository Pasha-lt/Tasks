# Нужно отсеить в списке числа меньшие и раные 5
a = [3, 3, 3, 4, 5, 7, 7, 8, 9, 0, 5, 5, 5, 7, 8, 9, 132]
b = filter(lambda x: x>5, a)
print(list(b))

# Нужно поменять местами ключи и значения в словаре
c = {123:'123', (12,23,4):12, 'kie':'ffds'}
d = {x:y for y,x in c.items()}
print(d)

# Напишите программу которая будет считать факториал, используйте функциональное программирование. 
from functools import reduce

number = int(input("Введите число с которого мы будем брать факториал: "))
numbers_list = range(1, number+1)
factorial = reduce(lambda x,y:x*y, numbers_list)
print(factorial)



