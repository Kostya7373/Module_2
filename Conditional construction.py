



first = input('Введите первое целое число ')
if first.isnumeric(): # проверяем что введено именно число
    first = int(first)
else:
    print('Можно вводить только числа')
print('Вы ввели тип: ' , type(first))

second = input('Введите второе  целое число ')
if second.isnumeric():
    second = int(second)
else:
    print('Можно вводить только числа')
print('Вы ввели тип: ' , type(second))

third = input('Введите третье целое число ')
if third.isnumeric():
    third = int(third)
else:
    print('Можно вводить только числа')
print('Вы ввели тип: ' ,type( third))
print('------------')
print('Вы ввели ',first,second,third)

if first == second == third :
    print('Всего одинаковых чисел ',3)
elif first == second or second == third or first == third :
    print('Всего одинаковых чисел ', 2)
else:
    print('Всего одинаковых чисел ',0)
