#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math

x1 = float(input('x1 - '))
y1 = float(input('y1 - '))
x2 = float(input('x2 - '))
y2 = float(input('y2 - '))

result = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
distance = round(result, 2)
print(distance)
