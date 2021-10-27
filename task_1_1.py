#1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
#Формат вывода результата:

#до минуты: <s> сек;
#до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
#в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#Примеры/Тесты:

#duration = 53: 53 сек
#duration = 153: 2 мин 33 сек
#duration = 4153: 1 час 9 мин 13 сек
#duration = 400153: 4 дн 15 час 9 мин 13 сек

sec_on_minute = 60
sec_on_hour = 3600
sec_on_day = 86400

user_variant = int(input("Введите количество секунд "))
day = user_variant // sec_on_day
remain_of_day = user_variant - day * sec_on_day
hour = remain_of_day // sec_on_hour
remain_of_hour = user_variant - (day * sec_on_day) - (hour * sec_on_hour)
minute = remain_of_hour //sec_on_minute
second = user_variant - (day * sec_on_day) - (hour * sec_on_hour) - (minute * sec_on_minute)



print("В " + str(user_variant) + " секундах: " + str(day) + " дней, " + str(hour) + " часов, " + str(minute) + " минут, " + str(second) + " секунд")
