# Создайте программу для игры с конфетами человек против компьютера.
from random import randint as randint

numsOfCandies = 2021
max_take = 28
counter = 0


def player_choice(numsOfCandies):
    if numsOfCandies == 0:
        return -1
    takenCandies = int(input("Enter how many candies you are taking away: "))
    while takenCandies <= 0 or takenCandies > max_take:
        takenCandies = int(input(f'You can take between 1 and {max_take} candies, please try again :'))
        if numsOfCandies < takenCandies:
            print(f' {numsOfCandies} candies are left , take a candies between 1 and {numsOfCandies}')
    if numsOfCandies < takenCandies:
        while takenCandies <= 0 or takenCandies > numsOfCandies:
            takenCandies = int(
                input(f'{numsOfCandies} candies are left, take a candies between 1 and {numsOfCandies}: '))
    numsOfCandies -= takenCandies
    return numsOfCandies


# Добавление другой метода для выбора копмьютером значений.
def computer_choice(numsOfCandies):
    bot_take = numsOfCandies % (max_take + 1)
    if bot_take % 2 == 0:
        bot_take = randint(1, max_take)
    numsOfCandies -= bot_take
    print(f'Computer takes {bot_take} candies. Candies left: {numsOfCandies}')
    return numsOfCandies


while numsOfCandies > 0:
    if numsOfCandies > 0:
        message1 = 'Player move'
        print(message1.center(50, '.'))
        numsOfCandies = player_choice(numsOfCandies)
        counter += 1
    if numsOfCandies > 0:
        message1 = 'Computer move'
        print(message1.center(50, '.'))
        numsOfCandies = computer_choice(numsOfCandies)
        counter += 1
if counter % 2 == 0:
    print('Computer wins')
else:
    print('Player wins')
