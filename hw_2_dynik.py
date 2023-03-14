import random
#
# # Task 1
# print('Task 1')
# min_num = random.randrange(60)
# quarter = 0
#
# if min_num < 15:
#     quarter = 1
# elif min_num < 30:
#     quarter = 2
# elif min_num < 45:
#     quarter = 3
# else:
#     quarter = 4
#
# print(f'{min_num} is in {quarter} quarter')
#
# # Task 2
# print('Task 2')
# birth_month = int(input('Номер місяця вашого народження:'))
#
# if 0 < birth_month <= 2 or birth_month == 12:
#     print('Зима - За вікном падав сніг.')
# elif 3 <= birth_month <= 5:
#     print('Весна - Все довкола розцвітало.')
# elif 6 <= birth_month <= 8:
#     print('Літо - Діти насолоджувались літніми канікулами.')
# elif 9 <= birth_month <= 11:
#     print('Осінь - Все довкола загоралось яскравими фарбами.')
# else:
#     print('Тільки цілі числа (1 - 12)')
#
# # Task 3
# print('Task 3')
# number = random.randint(0, 999)
#
# hundreds = number//100
# tens = (number % 100)//10
# nums = number % 10
# sum_of_all_nums = hundreds + tens + nums
#
# if sum_of_all_nums % 3 == 0 or nums % 2 == 0:
#     print(f'Число {number} ділиться на 6')
# else:
#     print(f'Число {number} не ділиться на 6')

# Task 4
print('Task 4')
x = float(input('Enter x:'))
y = float(input('Enter y:'))

if x > 0 and y > 0:
    print(f'Координати {x}:{y} належать до I чверті')
elif x > 0 and y < 0:
    print(f'Координати {x}:{y} належать до II чверті')
elif x < 0 and y < 0:
    print(f'Координати {x}:{y} належать до III чверті')
elif x < 0 and y > 0:
    print(f'Координати {x}:{y} належать до IV чверті')
elif x < 0 and y > 0:
    print(f'Координати {x}:{y} належать до IV чверті')
elif x == 0 and y == 0:
    print(f'Координати {x}:{y} належать самому центру')
else:
    print('Enter only digits')
