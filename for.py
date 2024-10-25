#for i in range(1,11): # start, stop, step
#   for j in range(1,11):
#        print(f'{i}x{j}={i*j}')

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []

n= 0 # проверяемое число
i=0 # задаем счетчик
j=0 # задаем счетчик

for i in range(len(numbers)): # перебор от (0) до (количество элементов)
    n = numbers[i] # выбираем элемент из списка (проверяемое число)

    if n < 2: # не(0) и не(1)
        print(n, 'не простое и несложное число')
        continue
    elif n == 2: # простое число
        primes.append(n)
        continue

    for j in range(2,n+1): # первый делитель (2) (перебираем делители, делим число на делитель)
        if (n % j == 0 )  and (j!= n) :
            not_primes.append(n) # является составным
            break
        elif ( n % j != 0): #остаток неравен (0)
            continue
        else:
            primes.append(n) # является простым



print('наши числа ',numbers)
print('простые числа ',primes)
print('составные числа ',not_primes)





