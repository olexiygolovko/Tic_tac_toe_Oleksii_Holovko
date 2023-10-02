from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

def greet():
    print("--------------------")
    print(Back.MAGENTA + Fore.BLACK + " Welcome to the game ")
    print(Back.MAGENTA + Fore.BLACK + "  tic-tac-toe  ")
    print(Back.MAGENTA + "--------------------")
    print(Back.MAGENTA + Fore.BLACK + " input format: x y ")
    print(Back.MAGENTA + Fore.BLACK + " separated by space  ")
    print(Back.MAGENTA + Fore.BLACK + " x - line number  ")
    print(Back.MAGENTA + Fore.BLACK + " y - column number ")
    print("--------------------")

greet()

player_name_x = input("Enter the name of the player playing with X ")
player_name_o = input("Enter the name of the player playing with Y ")


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
        cords = input(" Your move: ").split()

        if len(cords) != 2:
            print("Enter 2 coordinates!")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Enter numbers! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Out of range! ")
            continue

        if field[x][y] != " ":
            print(" The cage is occupied! ")
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
            print(f"Won {player_name_x}! Congratulations!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print(f"Won {player_name_o}! Congratulations!!!")
            return True
    return False


greet()

count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(f" Move: {player_name_x} (X) ")
    else:
        print(f" Move: {player_name_o} (0) ")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Draw! Friendship won!")
        break





