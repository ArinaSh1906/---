import os
import colorama


# победные комбинации
WIN_COMBINATIONS = (
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7)
)

# цвета
X_COLOR = colorama.Fore.LIGHTRED_EX
O_COLOR = colorama.Fore.LIGHTCYAN_EX
TEXT_COLOR = colorama.Fore.MAGENTA
BOARD_COLOR = colorama.Fore.WHITE

# список позиций на доске
board = list(range(1, 10))

# приветствие
print(TEXT_COLOR + 'Добро пожаловать в игру!')

# вывод игрового поля
for i in range(0, 7, 3):
    print(f'{BOARD_COLOR}[{board[i]}{BOARD_COLOR}] [{board[i + 1]}{BOARD_COLOR}] [{board[i + 2]}{BOARD_COLOR}]')


# счётчик ходов
turn = 0
# переключатель победы
is_win = False


# пока не победа:
while not is_win:
    # если ход чётный - крестик, нечётный - нолик
    if turn % 2 == 0:
        player_sign = X_COLOR + 'X'
    else:
        player_sign = O_COLOR + 'O'
    # ввод с консоли позиции на доске
    place = int(input(f'{TEXT_COLOR}Ходит {player_sign} \n{TEXT_COLOR}Введите позицию на доске: '))
    # если клетка свободна
    if board[place - 1] != X_COLOR + 'X' and board[place - 1] != O_COLOR + 'O':
        # очищаем консоль
        os.system('cls')
        # ставим знак игрока на доску
        board[place - 1] = player_sign
        # смена хода
        turn += 1
        # проверка, не победа ли
        if turn >= 5:
            # для каждой комбинации в кортеже победных комбинаций
            for combination in WIN_COMBINATIONS:
                # если элементы на доске для этой комбинации одинаковые:
                if board[combination[0] - 1] == board[combination[1] - 1] == board[combination[2] - 1]:
                    print(f'{TEXT_COLOR}Победил {player_sign}!')
                    is_win = True
                    # если пользователь вводит restart: 1) is_win = False 2) board = list(range...) 3) turn = 0
                    command = input(f'{TEXT_COLOR}Чтобы сыграть ещё раз, введите restart: ')
                    if command == 'restart':
                        is_win = False
                        board = list(range(1, 10))
                        turn = 0
                    break
            else:
                # else у цикла выполняется, если он закончился без break
                if turn == 9:
                    print(f'{TEXT_COLOR}Ничья')
                    is_win = True
    else:
        print(TEXT_COLOR + 'Клетка занята')

    for i in range(0, 7, 3):
        print(f'{BOARD_COLOR}[{board[i]}{BOARD_COLOR}] [{board[i + 1]}{BOARD_COLOR}] [{board[i + 2]}{BOARD_COLOR}]')

input(f'{TEXT_COLOR}Для выхода нажмите Enter')
