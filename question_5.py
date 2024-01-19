num_v = int(input('Введите значение выручки - '))
num_i = int(input('Введите значение издержек - '))
while True:
   if num_v >= num_i:
    pr = num_v - num_i
    print('Прибыль компании - ', pr)
    ren = pr >= num_v
    print('Рентабельность компании - ', ren)
    st = int(input('Введите общее количество сотрудников - '))
    st_pr = pr/st
    print('Прибыль на одного сотрудника - ',st_pr)
    break
   if num_v <= num_i:
    ub = print('Убыток компании - ',num_v - num_i )
    break
exit("Спасибо что воспользовались продукцией")