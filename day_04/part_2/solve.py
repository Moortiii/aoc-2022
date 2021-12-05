import json

FILENAME = "input.txt"
#FILENAME = "example.txt"
SIZE = 5

with open(FILENAME, "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

numbers_to_draw = data[0].split(",")
board_input = data[2:]

boards = {}
board_count = 0
cells = []

board = {
    "id": board_count,
    "cells": [],
    "has_won": False
}

x = 0
y = -1

for line in board_input:
    y += 1

    if line == "":
        boards[board_count] = board
        board_count += 1

        x = 0
        y = -1

        board = {
            "id": board_count,
            "cells": [],
            "has_won": False
        }
        continue

    numbers = line.split(" ")
    numbers = [x for x in numbers if x != ""]

    for number in numbers:
        x = x if x != 5 else 0
        y = y if y != 5 else 0

        board["cells"].append({
            "x": x,
            "y": y,
            "marked": False,
            "value": number
        })

        x += 1

# Add the final board
boards[board_count] = board


def get_cell(board, x, y):
    matches = [
        cell if (cell["x"] == x and cell["y"] == y) else None
        for cell in board["cells"]
    ]

    return [cell for cell in matches if cell != None][0]


def check_if_winner(board):
    # Check horizontally
    for y in range(0, SIZE):
        winner = True

        for x in range(0, SIZE):
            cell = get_cell(board, x, y)

            if cell["marked"] != True:
                winner = False

        if winner == True:
            return True

    # Check vertically
    for x in range(0, SIZE):
        winner = True

        for y in range(0, SIZE):
            cell = get_cell(board, x, y)

            if cell["marked"] != True:
                winner = False

        if winner == True:
            return True

    return False


for number in numbers_to_draw:
    for key, board in boards.items():
        for cell in board["cells"]:
            if cell["value"] == number:
                cell["marked"] = True

                if check_if_winner(board):
                    print(f"Board {key} won with number {number}")
                    board["has_won"] = True

                    if all([True if board["has_won"] else False for board in boards.values()]):
                        print("Board: " + str(key), "is the last to win.")
                        sum = 0

                        for cell in board["cells"]:
                            if cell["marked"] == False:
                                sum += int(cell["value"])

                        print("Sum:", sum)
                        print("Result:", sum * int(number))
                        import sys
                        sys.exit(0)
