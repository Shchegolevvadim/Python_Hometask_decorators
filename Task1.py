#Напишите следующие функции:
#Нахождение корней квадратного уравнения
#Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
#Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
#Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.



from typing import Callable
import random
def sqrt(a: int, b: int, c: int):
    d = b**2 - 4 * a * c
    x1 = (-b - d**0.5)/2*a
    x2 = (-b + d**0.5)/2*a

