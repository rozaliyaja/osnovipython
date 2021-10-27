numbers = 1000
num = 0 # вводим переменную чтобы проверить на нечетность
result = 0 # сюда будем записывать результат
while num <= numbers:
    sum_num = 0 # сумма цифр  кубов
    if num % 2 != 0: # если число нечетное
        new_num = num ** 3 #  то возводим его в куб
        while new_num / 10 != 0: # пока куб числа остаток от деления на 10 не равен 0
            sum_num = sum_num + new_num % 10 # отделяем последний символ в числе
            new_num = new_num // 10 # уменьшаем число
        if sum_num % 7 == 0:
            result = result + num
            print(num, '^3: ', (num ** 3), ' summ ', sum_num, num )
        num = num + 1

    else:
        num = num + 1
