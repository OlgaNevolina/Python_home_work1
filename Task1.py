#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#*Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет

day = int(input('Введите число дня недели '))
if day > 7 or day < 1:
    print('Повторите ввод')
elif day == 7 or day == 6:
    print('Да')
else:
    print('Нет')
    