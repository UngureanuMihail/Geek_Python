# Создайте программу для игры с конфетами человек против компьютера.
from random import randint as randint

numsOfCandies = 2021
counter = 0


def player_choice(numsOfCandies):
    if numsOfCandies == 0:
        return -1
    takenCandies = int(input("Enter how many candies you are taking away: "))
    while takenCandies <= 0 or takenCandies > 28:
        takenCandies = int(input('You can take between 1 and 28 candies, please try again :'))
        if numsOfCandies < takenCandies:
            print(f' {numsOfCandies} candies are left , take a candies between 1 and {numsOfCandies}')
    if numsOfCandies < takenCandies:
        while takenCandies <= 0 or takenCandies > numsOfCandies:
            takenCandies = int(input(f'{numsOfCandies} candies are left, take a candies between 1 and {numsOfCandies}: '))
    numsOfCandies -= takenCandies
    return numsOfCandies


def computer_choice(numsOfCandies):
    takenCandies = randint(1, 28)
    while takenCandies > numsOfCandies:
        takenCandies = randint(1, 28)
    if numsOfCandies <= 28:
        takenCandies = numsOfCandies
    if 28 < numsOfCandies < 56:
        takenCandies = numsOfCandies - 29
    numsOfCandies -= takenCandies
    print(f'Computer takes {takenCandies} candies. Candies left: {numsOfCandies}')
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
