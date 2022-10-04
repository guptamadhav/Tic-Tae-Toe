import os

def clear():
    os.system('cls')


GRID = ["_", "_", "_",
        "_", "_", "_",
        "_", "_", "_"]
# format :0 1 2
#         3 4 5
#         6 7 8

win_series = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def check_win():
    for i in win_series:
        if GRID[i[0]] == GRID[i[1]] == GRID[i[2]] and GRID[i[0]] != "_":
            return True



win = False

while not win:
    clear()
    print(f"{GRID[0]} | {GRID[1]} | {GRID[2]}\n------------\n{GRID[3]} | {GRID[4]} | {GRID[5]}\n------------\n{GRID[6]} | {GRID[7]} | {GRID[8]}")
    user1_X = int(input("(User 1)Enter your move: ")) - 1
    if GRID[user1_X] == "_":
        GRID[user1_X] = "X"
    else:
        continue
    if check_win():
        print(f"{GRID[0]} | {GRID[1]} | {GRID[2]}\n------------\n{GRID[3]} | {GRID[4]} | {GRID[5]}\n------------\n{GRID[6]} | {GRID[7]} | {GRID[8]}")
        print("User 1 wins")
        break

    print(f"{GRID[0]} | {GRID[1]} | {GRID[2]}\n------------\n{GRID[3]} | {GRID[4]} | {GRID[5]}\n------------\n{GRID[6]} | {GRID[7]} | {GRID[8]}")

    user2_O = int(input("(User 2)Enter your move: ")) - 1
    if GRID[user2_O] == "_":
        GRID[user2_O] = "O"
    else:
        continue
    if check_win():
        print(f"{GRID[0]} | {GRID[1]} | {GRID[2]}\n------------\n{GRID[3]} | {GRID[4]} | {GRID[5]}\n------------\n{GRID[6]} | {GRID[7]} | {GRID[8]}")
        print("User 2 wins")
        break
