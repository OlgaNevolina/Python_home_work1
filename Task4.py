#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#*Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

number = int(input('Введите номер четверти плоскости: '))
if number == 1:
    print('x > 0 and y > 0')
elif number == 2:
    print('x < 0 and y > 0')
elif number == 3:
    print('x < 0 and y < 0')
elif number == 4:
    print('x > 0 and y < 0')
else:
    print('Нет такой плоскости') 
