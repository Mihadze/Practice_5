import random

baza = {
    'Эфиопия': 'Аддис-Абеба',
    'Шри-Ланка': 'Шри-Джаяварденепура-Котте',
    'Тринидад и Тобаго': 'Порт-оф-Спейн',
    'Танзания': 'Дар-эс-Салам',
    'Свазиленд': 'Лобамба',
    'Малайзия': 'Аддис-Абеба',
    'Колумбия': 'Санта-Фе-Де-Богота',
    'Исландия': 'Рейкьявик',
    'Гондурас': 'Тегусигальпа',
    'Бруней': 'Бандар-Сери-Бегаван',
    }

countries = list(baza.items())
score = 0
number = 0




while number < 5:
    a = list(random.choice(countries))
    cap_city = a[1]  
    print('Введите столицу', a[0], ':')
    my_cap_city = str(input())
    if my_cap_city == cap_city:
        score += 1
        number += 1
        print('Ответ верен')
    else:
        number += 1
        print('К сожалению не верно, попробуй ещё раз')
print('Твой результат: ', score)
