time = int(input('Введите время в секундах - '))
def convert (seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return '%d:%02d:%02d' % (hour, minutes,seconds)
print('Результат введенного значения в формате чч:мм:сс - ', convert(time))
exit("Спасибо что воспользовались продукцией")