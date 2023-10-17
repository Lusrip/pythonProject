n = int(input('Введите загаданное число n - '))
temp = str (n)
t1 = temp + temp
t2 = temp + temp + temp
answer = n + int(t1) + int (t2)
print('Результат вашего загаданного чила - ', answer)