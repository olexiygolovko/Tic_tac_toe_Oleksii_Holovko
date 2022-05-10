from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

def greet():
    print("--------------------")
    print(Back.MAGENTA + Fore.BLACK + " Приветсвуем в игре ")
    print(Back.MAGENTA + Fore.BLACK + "  крестики-нолики   ")
    print(Back.MAGENTA + "--------------------")
    print(Back.MAGENTA + Fore.BLACK + " формат ввода: x y  ")
    print(Back.MAGENTA + Fore.BLACK + " через пробел       ")
    print(Back.MAGENTA + Fore.BLACK + " x - номер строки   ")
    print(Back.MAGENTA + Fore.BLACK + " y - номер столбца  ")
    print("--------------------")

greet()

player_name_x = input("Введите имя игрока играющего крестиком: ")
player_name_o = input("Введите имя игрока играющего ноликом: ")


field = [[" "] * 3 for i in range(3)]

def show():
    print()
    print(Back.MAGENTA + Fore.BLACK + "    | 0 | 1 | 2 | ")
    print(Back.MAGENTA + Fore.BLACK + "  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(Back.MAGENTA + Fore.BLACK + row_str)
        print(Back.MAGENTA + Fore.BLACK + "  --------------- ")
    print()

show()

def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Вышли за рамки диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        show()
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(f"Выиграл {player_name_x}! Поздравляем!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print(f"Выиграл {player_name_o}! Поздравляем!!!")
            return True
    return False


greet()

count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(f" Ходит {player_name_x} (крестик) ")
    else:
        print(f" Ходит {player_name_o} (нолик) ")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья! Победила дружба!")
        break





