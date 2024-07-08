first = int(input('Введите первое число:'))  # Вводим первое число
second = int(input('Введите второе число:'))  # Вводим второе число
third = int(input('Введите третье число:'))  # Вводим третье число
if first == second == third:
    print('Все числа равны:', 3)
elif first == second or second == third or third == first:
    print('Два числа равны:', 2)
else:
    print('Одинаковых чисел нет:', 0)
