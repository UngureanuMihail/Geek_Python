# Игра в крестики нолики
import random

print('Welcome to Tic Tac Toe game'.center(50, '-'))
# Доступные номера для выбора
possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Игральная доска
rows = 3  # строки
cols = 3  # стоблцы


# Функция для рисования доски
def print_game_board():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
    print("\n+---+---+---+")

   
# Функция для определения победителя
def check_for_winner(gameBoard):
    # По оси Х
    if gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X':
        print("Пользователь победил!")
        return "X"
    elif gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O':
        print("Компьютер победил!")
        return "O"
    elif gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X':
        print("Пользователь победил!")
        return "X"
    elif gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O':
        print("Компьютер победил!")
        return "O"
    elif gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X':
        print("Компьютер победил!")
        return "X"
    elif gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O':
        print("Компьютер победил!")
        return "O"
    # По оси У
    if gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X':
        print("Пользователь победил!")
        return "X"
    elif gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O':
        print("Компьютер победил!")
        return "O"
    elif gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X':
        print("Пользователь победил!")
        return "X"
    elif gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O':
        print("Компьютер победил!")
        return "O"
    elif gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X':
        print("Пользователь победил!")
        return "X"
    elif gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O':
        print("Компьютер победил!")
        return "O"
    # По диагонали
    elif gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X':
        print("Пользователь победил!")
        return "X"
    elif gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O':
        print("Компьютер победил!")
        return "O"
    elif gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X':
        print("Пользователь победил!")
        return "X"
    elif gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O':
        print("Компьютер победил!")
        return "O"
    else:
        return "N"


# Фунция для хода (изменение доски)
def modify_array(num, turn):
    num -= 1
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    elif num == 5:
        gameBoard[1][2] = turn
    elif num == 6:
        gameBoard[2][0] = turn
    elif num == 7:
        gameBoard[2][1] = turn
    elif num == 8:
        gameBoard[2][2] = turn


finish = False
turnCounter = 0

while not finish:
    # Ход пользователя
    if turnCounter % 2 == 0:  # В случае остатка деления значения хода на 2 == 0, значит ход пользовтеля
        print_game_board()
        numberPicked = int(input("\nВведите цифру [1-9]: "))  # Ввод числа
        if numberPicked >= 1 or numberPicked <= 9:  # Условине для ввода числа из диапазона
            modify_array(numberPicked, 'X')  # Изменение доски
            possibleNumbers.remove(numberPicked)  # Удаление номера из списка возможных
        else:
            print("Неверное число. Пожалуйста попробуйте еще раз.")  # В другом случае сообщение о ошибке
        turnCounter += 1

    # Ход компьютера
    else:
        while True:
            cpu_choice = random.choice(possibleNumbers)  # Случайный выбор комьютера
            print("\nВыбор компьютера: ", cpu_choice)
            if cpu_choice in possibleNumbers:
                modify_array(cpu_choice, 'O')
                possibleNumbers.remove(cpu_choice)  # Удаление номера из списка возможных
                turnCounter += 1
                break

    winner = check_for_winner(gameBoard)
    if winner != "N":
        print("\nКонец. Спасибо за игру :)")
        break
