# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.

numsOfCandies = 2021
counter = 0


def player_choice(numsOfCandies):
    if numsOfCandies == 0:
        return print('Error occured')

    take_candies = int(input("Enter how many candies you are taking away: "))
    while take_candies <= 0 or take_candies > 28:
        take_candies = int(input('You can take between 1 and 28 candies, please try again'))
        if numsOfCandies < take_candies:
            print(f' {numsOfCandies} candies are left , take a candies between 1 and {numsOfCandies}')
    if numsOfCandies < take_candies:
        while take_candies <= 0 or take_candies > numsOfCandies:
            take_candies = int(input(f'осталось {numsOfCandies} конфет, введите число от 1 до {numsOfCandies}: '))
    numsOfCandies -= take_candies
    return numsOfCandies


while numsOfCandies > 0:
    if numsOfCandies > 0:
        message1 = 'Player I move'
        print(message1.center(50, '.'))
        numsOfCandies = player_choice(numsOfCandies)
        counter += 1
    if numsOfCandies > 0:
        message2 = 'Player II move'
        print(message2.center(50, '.'))

        numsOfCandies = player_choice(numsOfCandies)
        counter += 1
if counter % 2 == 0:
    print('Player II wins !!!')
else:
    print('Player I wins !!!')
