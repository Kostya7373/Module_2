my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] # дан список my_list
a = len(my_list) # количество элементов в списке
print('количество элементов в списке ', a)
b = 0 # переменная для цикла
while b < a : # выод на экран ТОЛЬКО ПОЛОЖИТЕЛЬНЫХ чисел (до отрицательного либо до конца)
    if my_list[b] > 0 :
        print(my_list[b])
        b += 1
        continue
    elif my_list[b] == 0 :
        b += 1
        continue
    else :
        break





