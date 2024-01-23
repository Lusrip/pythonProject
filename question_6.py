a = int(input('Первоначальные километры - '))
resault = a * 0.1
b = int(input('Цель спортсменна - '))
 while True:
    resault += 1
    if resault >= b:
        #инструкия по полученному результату
        break
    elif resault <= b:
        #инструкция по продолжению подсчета
        continue
    print("Спортсмен пробежал", b, "километров на день - ", resault)